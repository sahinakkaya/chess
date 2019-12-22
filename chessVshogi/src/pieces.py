from chessVshogi.src.directions import Direction, SetOfVectors, Vector2D
from PyQt5.QtCore import QObject, pyqtSignal


class Piece(QObject):
    """
    Base class for a piece in the game
    """
    PRIMARY_MOVE = None
    SECONDARY_MOVE = None
    CAPTURE_MOVE = None
    possible_moves_found = pyqtSignal(SetOfVectors)

    def __init__(self, board, x, y, promotable=False,
                 has_promoted=False,
                 is_dead=False,
                 side="W"):
        super(Piece, self).__init__()
        self.board = board
        self.x = x
        self.y = y
        self.side = side
        self.promoting_rank = None
        self.is_moved = False
        self.promotable = promotable
        self.has_promoted = has_promoted
        self.is_dead = is_dead
        board.mouse_clicked.connect(self.get_possible_moves)
        board.piece_moved.connect(self.update_position)
        self.possible_moves_found.connect(board.set_possible_moves)

    @classmethod
    def name(cls):
        return cls.__name__

    def get_possible_moves(self, x, y, fromclickevent=True):
        """
        Return possible moves for the piece
        # TODO: Update this docstring
        :return: a set of Vector2D objects that a piece can go
        """
        if self.x == x and self.y == y:
            primary_movement, range_ = self.PRIMARY_MOVE
            possible_moves = self.get_moves_for_movement(primary_movement,
                                                         range_)

            if self.SECONDARY_MOVE:
                sec_movement, sec_range = self.SECONDARY_MOVE
                possible_moves = possible_moves | self.get_moves_for_movement(sec_movement, sec_range)
            for cap_move in self.CAPTURE_MOVE:
                board_size = self.board.state.board_size
                movement, range_ = cap_move
                for direction in movement:
                    if self.side == "B":  # as in Black
                        direction = reversed(direction)
                    for i in range(1, range_ + 1):
                        move = (direction * i) + Vector2D(self.x, self.y)
                        if (1, 1) <= move <= (board_size, board_size):
                            if self.board.is_empty(move.x, move.y):
                                continue
                            possible_moves.add(move)
                            break
            if fromclickevent:
                self.possible_moves_found.emit(possible_moves)
            else:
                return possible_moves

    def get_moves_for_movement(self, movement, range_):
        possible_moves = SetOfVectors()
        board_size = self.board.state.board_size
        for direction in movement:
            if self.side == "B":  # as in Black
                direction = reversed(direction)
            for i in range(1, range_ + 1):
                move = (direction * i) + Vector2D(self.x, self.y)
                if (1, 1) <= move <= (board_size, board_size):
                    if not self.board.is_empty(move.x, move.y):
                        break
                    possible_moves.add(move)
        return possible_moves

    def update_position(self, from_position, to_position, moved_piece):
        if from_position == (self.x, self.y):
            self.x, self.y = to_position
            if self.promotable:
                if (self.side == "W" and self.y >= self.promoting_rank) or \
                        (self.side == "B" and self.y <= self.promoting_rank):
                    self.promote_trigger()
                else:  # this segment will be required later.
                    prev_y = from_position[1]
                    if (self.side == "W" and prev_y >= self.promoting_rank) or \
                            (self.side == "B" and prev_y <= self.promoting_rank):
                        self.promote_trigger()
        elif to_position == (self.x, self.y):
            self.board.state.pieces_on_board.remove(self)
            self.board.mouse_clicked.disconnect(self.get_possible_moves)
            self.deleteLater()

    def promote_trigger(self):
        pass


class ChessPiece(Piece):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def promote_trigger(self):
        pass


class ShogiPiece(Piece):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.side == "W":
            self.promoting_rank = self.board.state.board_size - 2
        else:
            self.promoting_rank = 3

    def promote_trigger(self):
        print("Promotion_trigger_shogi_side:", self.side)
        promoted_self = eval("Promoted"+self.name())
        self.PRIMARY_MOVE = promoted_self.PRIMARY_MOVE
        self.SECONDARY_MOVE = promoted_self.SECONDARY_MOVE
        self.CAPTURE_MOVE = promoted_self.CAPTURE_MOVE
        board_tile = self.board.get_tile_at(self.x, self.y)
        board_tile.setProperty("Piece", board_tile.property("Piece")+"P")
        self.board.draw_board()
        self.promotable = False
        pass


class Pawn(ChessPiece):
    moved_double_square = pyqtSignal(int, int, int, int)
    promotion_trigger = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.PRIMARY_MOVE = [SetOfVectors(Direction.FORWARD), 2]
        self.CAPTURE_MOVE = [[Direction.HORIZONTAL & Direction.FORWARD, 1]]
        self.shadow = None
        self.promotable = True
        if self.side == "W":
            self.promoting_rank = self.board.state.board_size
        else:
            self.promoting_rank = 1
        self.moved_double_square.connect(self.board.handle_double_square_move)
        self.promotion_trigger.connect(self.board.handle_pawn_promotion)

    def update_position(self, from_position, to_position, moved_piece):
        self.shadow = None
        if from_position == (self.x, self.y):
            self.PRIMARY_MOVE[1] = 1
            difference = Vector2D(*to_position) - Vector2D(*from_position)
            if difference.y in (2, -2):
                summation = (Vector2D(*from_position) + Vector2D(*to_position))
                self.shadow = summation // 2
                self.moved_double_square.emit(*self.shadow, *to_position)
        elif Vector2D(*to_position) == self.shadow and moved_piece == "P":
            to_position = self.x, self.y
        super().update_position(from_position, to_position, moved_piece)

    def promote_trigger(self):
        print("Promoting Pawn")
        self.promotion_trigger.emit(self.side)
        pass


class Knight(ChessPiece):
    PRIMARY_MOVE = [SetOfVectors((2, 1), (1, 2)).flip(
        axes="h", in_place=True).flip(axes="v", in_place=True), 1]
    CAPTURE_MOVE = [PRIMARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Rook(ChessPiece):
    PRIMARY_MOVE = [Direction.STRAIGHT, 8]
    CAPTURE_MOVE = [PRIMARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Bishop(ChessPiece):
    PRIMARY_MOVE = [Direction.DIAGONAL, 8]
    CAPTURE_MOVE = [PRIMARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Queen(ChessPiece):
    PRIMARY_MOVE = [Direction.STRAIGHT | Direction.DIAGONAL, 8]
    CAPTURE_MOVE = [PRIMARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class King(ChessPiece):
    PRIMARY_MOVE = [Direction.STRAIGHT | Direction.DIAGONAL, 1]
    CAPTURE_MOVE = [PRIMARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class S_King(ShogiPiece):  # can be renamed to "Gyoku"
    PRIMARY_MOVE = [Direction.STRAIGHT | Direction.DIAGONAL, 1]
    CAPTURE_MOVE = [PRIMARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SRook(ShogiPiece):  # can be renamed to "Hisha"
    PRIMARY_MOVE = [Direction.STRAIGHT, 8]
    CAPTURE_MOVE = [PRIMARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.promotable = True


class SBishop(ShogiPiece):  # can be renamed to "Kaku"
    PRIMARY_MOVE = [Direction.DIAGONAL, 8]
    CAPTURE_MOVE = [PRIMARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.promotable = True


class Lance(ShogiPiece):  # can be renamed to "Kyo"
    PRIMARY_MOVE = [SetOfVectors(Direction.FORWARD), 8]
    CAPTURE_MOVE = [PRIMARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.promotable = True


class SKnight(ShogiPiece):  # can be renamed to "Kei" or "Forward Knight"
    PRIMARY_MOVE = [SetOfVectors((1, 2), ).flip(axes="h", in_place=True), 1]
    CAPTURE_MOVE = [PRIMARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.promotable = True


class SPawn(ShogiPiece):  # can be renamed to "Fu"
    PRIMARY_MOVE = [SetOfVectors(Direction.FORWARD), 1]
    CAPTURE_MOVE = [PRIMARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.promotable = True


class Silver(ShogiPiece):  # can be renamed to "Gin"
    PRIMARY_MOVE = [
        Direction.FORWARD | Direction.LDIAGONAL | Direction.RDIAGONAL, 1]
    CAPTURE_MOVE = [PRIMARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.promotable = True


class Gold(ShogiPiece):  # can be renamed to "Kin"
    PRIMARY_MOVE = [Direction.HORIZONTAL | Direction.VERTICAL | (
            Direction.HORIZONTAL & Direction.FORWARD), 1]
    CAPTURE_MOVE = [PRIMARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PromotedSPawn(ShogiPiece):  # can be renamed to "Tokin"
    PRIMARY_MOVE = Gold.PRIMARY_MOVE
    CAPTURE_MOVE = [PRIMARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PromotedLance(ShogiPiece):  # can be renamed to "Narikyo"
    PRIMARY_MOVE = Gold.PRIMARY_MOVE
    CAPTURE_MOVE = [PRIMARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PromotedSKnight(ShogiPiece):  # can be renamed to "NariKei"
    PRIMARY_MOVE = Gold.PRIMARY_MOVE
    CAPTURE_MOVE = [PRIMARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PromotedSilver(ShogiPiece):  # can be renamed to "Narigin"
    PRIMARY_MOVE = Gold.PRIMARY_MOVE
    CAPTURE_MOVE = [PRIMARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PromotedSRook(ShogiPiece):  # can be renamed to "Ryu" or "Dragon"
    PRIMARY_MOVE = [Direction.STRAIGHT, 8]
    SECONDARY_MOVE = [Direction.DIAGONAL, 1]
    CAPTURE_MOVE = [PRIMARY_MOVE,
                    SECONDARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PromotedSBishop(ShogiPiece):  # can be renamed to "Uma" or "Horse"
    PRIMARY_MOVE = [Direction.DIAGONAL, 8]
    SECONDARY_MOVE = [Direction.STRAIGHT, 1]
    CAPTURE_MOVE = [PRIMARY_MOVE,
                    SECONDARY_MOVE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
