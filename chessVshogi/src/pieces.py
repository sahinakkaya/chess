from chessVshogi.src.directions import Direction, SetOfVectors, Vector2D
from PyQt5.QtCore import QObject, pyqtSignal


class Piece(QObject):
    """
    Base class for a piece in the game
    """
    PRIMARY_MOVE = None
    SECONDARY_MOVE = None
    CAPTURE_MOVE = None

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
        self.name_ = ""

    @classmethod
    def name(cls):
        return cls.__name__

    def get_possible_moves(self):
        """
        Return possible moves for the piece
        # TODO: Update this docstring
        :return: a set of Vector2D objects that a piece can go
        """
        primary_movement, range_ = self.PRIMARY_MOVE
        possible_moves = self.get_moves_for_movement(primary_movement,
                                                     range_)

        if self.SECONDARY_MOVE:
            sec_movement, sec_range = self.SECONDARY_MOVE
            possible_moves = possible_moves | self.get_moves_for_movement(
                sec_movement, sec_range)
        for cap_move in self.CAPTURE_MOVE:
            board_size = self.board.state.board_size
            movement, range_ = cap_move
            for direction in movement:
                if self.side == "B":  # as in Black
                    direction = reversed(direction)
                for i in range(1, range_ + 1):
                    move = (direction * i) + Vector2D(self.x, self.y)
                    if (1, 1) <= move <= (board_size, board_size):
                        if self.board.is_empty(move.x, move.y,
                                               include_shadows=True):
                            continue
                        possible_moves.add(move)
                        break
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

    def set_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def __repr__(self):
        return self.name_

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
            self.promoting_rank = self.board.board_size - 2
        else:
            self.promoting_rank = 3

    def promote_trigger(self):
        from chessVshogi.src.ui_mapper import mapper
        print("Promotion_trigger_shogi_side:", self.side)
        promoted_self = eval("Promoted" + self.name())
        self.PRIMARY_MOVE = promoted_self.PRIMARY_MOVE
        self.SECONDARY_MOVE = promoted_self.SECONDARY_MOVE
        self.CAPTURE_MOVE = promoted_self.CAPTURE_MOVE
        piece = self.board.get_cell(self.x, self.y).piece
        # CAN BE MOVED SOMEWHERE ELSE TO AVOID IMPORT
        piece.name_ += "P"
        piece.resource = mapper[piece.name_]["resource"]
        self.board.draw_board()
        self.promotable = False
        pass


class Pawn(ChessPiece):
    moved_double_square = pyqtSignal(int, int, int, int)
    promotion_trigger = pyqtSignal(QObject)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.PRIMARY_MOVE = [SetOfVectors(Direction.FORWARD), 2]
        self.CAPTURE_MOVE = [[Direction.HORIZONTAL & Direction.FORWARD, 1]]
        self.shadow = None
        self.promotable = True
        if self.side == "W":
            self.promoting_rank = self.board.board_size
        else:
            self.promoting_rank = 1
        self.moved_double_square.connect(self.board.handle_double_square_move)
        self.promotion_trigger.connect(self.board.handle_pawn_promotion)

    def set_position(self, new_x, new_y):
        self.PRIMARY_MOVE[1] = 1
        difference = Vector2D(new_x, new_y) - Vector2D(self.x, self.y)
        if difference.y in (2, -2):
            summation = Vector2D(new_x, new_y) + Vector2D(self.x, self.y)
            self.shadow = summation // 2
            self.moved_double_square.emit(*self.shadow, new_x, new_y)
        super().set_position(new_x, new_y)

    def promote_trigger(self):
        print("Promoting Pawn")
        self.promotion_trigger.emit(self)
        pass

    def transform(self):
        from chessVshogi.src.ui_mapper import mapper
        self.name_ = self.name_[:3] + self.sender().objectName()[0] + self.name_[4:]
        self.resource = mapper[self.name_]["resource"]
        promoted_self = eval(self.sender().objectName())
        self.PRIMARY_MOVE = promoted_self.PRIMARY_MOVE
        self.SECONDARY_MOVE = promoted_self.SECONDARY_MOVE
        self.CAPTURE_MOVE = promoted_self.CAPTURE_MOVE
        self.promotable=False
        self.sender().parent().close()
        self.sender().parent().deleteLater()
        self.board.draw_board()


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
