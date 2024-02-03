from chess.src.directions import Direction, SetOfVectors, Vector2D
from PyQt6.QtCore import QObject, pyqtSignal


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
        if self.promotable:
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
        import chess.src.ui_mapper as ui_mapper
        mapper = ui_mapper.mapper()
        name_mapping = {
            "Knight": "N",
            "Queen": "Q",
            "Rook": "R",
            "Bishop": "B"
        }
        self.name_ = self.name_[:3] + name_mapping[self.sender().objectName()] + self.name_[4:]
        self.resource = mapper[self.name_]["resource"]
        promoted_self = eval(self.sender().objectName())
        self.PRIMARY_MOVE = promoted_self.PRIMARY_MOVE
        self.SECONDARY_MOVE = promoted_self.SECONDARY_MOVE
        self.CAPTURE_MOVE = promoted_self.CAPTURE_MOVE
        self.promotable = False
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
