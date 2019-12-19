from chessVshogi.directions import Direction, SetOfVectors, Vector2D
from PyQt5.QtCore import QObject, pyqtSignal


class Piece(QObject):
    """
    Base class for a piece in the game
    """
    PRIMARY_MOVE = [SetOfVectors(), 1]
    SECONDARY_MOVE = None
    CAPTURE_MOVE = None
    possible_moves_found = pyqtSignal(SetOfVectors)

    def __init__(self, board, x, y, promotable=False,
                 has_promoted=False,
                 is_dead=False):
        super(Piece, self).__init__()
        self.CAPTURE_MOVE = self.PRIMARY_MOVE
        self.board = board
        self.x = x
        self.y = y
        self.side = "W"  # as in White
        self.is_moved = False
        self.promotable = promotable
        self.has_promoted = has_promoted
        self.is_dead = is_dead
        self.get_possible_moves = self.get_possible_moves
        board.mouse_clicked.connect(self.get_possible_moves)
        board.piece_moved.connect(self.update_position)
        self.possible_moves_found.connect(board.set_possible_moves)

    @classmethod
    def name(cls):
        return cls.__name__

    def get_possible_moves(self, x, y):
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
                possible_moves.add(
                    self.get_moves_for_movement(*self.SECONDARY_MOVE))
            if self.CAPTURE_MOVE:
                board_size = self.board.state.board_size
                movement, range_ = self.CAPTURE_MOVE
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

            self.possible_moves_found.emit(possible_moves)

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

    def update_position(self, from_position, to_position):
        if from_position == (self.x, self.y):
            print("called!", self.name())
            self.x, self.y = to_position
        elif to_position == (self.x, self.y):
            self.board.mouse_clicked.disconnect(self.get_possible_moves)
            self.deleteLater()


class ChessPiece(Piece):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ShogiPiece(Piece):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Pawn(ChessPiece):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.PRIMARY_MOVE = [SetOfVectors(Direction.FORWARD), 2]
        self.CAPTURE_MOVE = [Direction.HORIZONTAL & Direction.FORWARD, 1]

    def update_position(self, from_position, to_position):
        if from_position == (self.x, self.y):
            print(self.x, self.y, "yes")
            self.PRIMARY_MOVE[1] = 1
        super().update_position(from_position, to_position)

# class BlackPawn(ChessPiece):
#     MOVEMENT = Direction.BACKWARD | (
#             Direction.HORIZONTAL & Direction.BACKWARD)
#     MOVEMENT_RANGE = 2
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)


class Knight(ChessPiece):
    PRIMARY_MOVE = [SetOfVectors((2, 1), (1, 2)).flip(
        axes="h", in_place=True).flip(axes="v", in_place=True), 1]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Rook(ChessPiece):
    PRIMARY_MOVE = [Direction.STRAIGHT, 8]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Bishop(ChessPiece):
    PRIMARY_MOVE = [Direction.DIAGONAL, 8]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Queen(ChessPiece):
    PRIMARY_MOVE = [Direction.STRAIGHT | Direction.DIAGONAL, 8]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class King(ChessPiece):
    PRIMARY_MOVE = [Direction.STRAIGHT | Direction.DIAGONAL, 1]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class S_King(ShogiPiece):  # can be renamed to "Gyoku"
    PRIMARY_MOVE = [Direction.STRAIGHT | Direction.DIAGONAL, 1]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class S_Rook(ShogiPiece):  # can be renamed to "Hisha"
    PRIMARY_MOVE = [Direction.STRAIGHT, 8]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class S_Bishop(ShogiPiece):  # can be renamed to "Kaku"
    PRIMARY_MOVE = [Direction.DIAGONAL, 8]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Lance(ShogiPiece):  # can be renamed to "Kyo"
    PRIMARY_MOVE = [SetOfVectors(Direction.FORWARD), 8]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class S_Knight(ShogiPiece):  # can be renamed to "Kei" or "Forward Knight"
    PRIMARY_MOVE = [SetOfVectors((1, 2), ).flip(axes="h", in_place=True), 1]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class S_Pawn(ShogiPiece):  # can be renamed to "Fu"
    PRIMARY_MOVE = [SetOfVectors(Direction.FORWARD), 1]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Silver(ShogiPiece):  # can be renamed to "Gin"
    PRIMARY_MOVE = [Direction.FORWARD | Direction.LDIAGONAL | Direction.RDIAGONAL, 1]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Gold(ShogiPiece):  # can be renamed to "Kin"
    PRIMARY_MOVE = [Direction.HORIZONTAL | Direction.VERTICAL | (
            Direction.HORIZONTAL & Direction.FORWARD), 1]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Promoted_Pawn:  # can be renamed to "Tokin"
    PRIMARY_MOVE = Gold.PRIMARY_MOVE
    MOVEMENT_RANGE = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Promoted_Lance:  # can be renamed to "Narikyo"
    PRIMARY_MOVE = Gold.PRIMARY_MOVE
    MOVEMENT_RANGE = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Promoted_Knight:  # can be renamed to "NariKei"
    PRIMARY_MOVE = Gold.PRIMARY_MOVE
    MOVEMENT_RANGE = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Promoted_Silver:  # can be renamed to "Narigin"
    PRIMARY_MOVE = Gold.PRIMARY_MOVE
    MOVEMENT_RANGE = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# TODO: Need to define special cases where one direction of movement is limited in range
# class Promoted_Rook:  # can be renamed to "Ryu" or "Dragon"
#     MOVEMENT = Rook.MOVEMENT
#     MOVEMENT_RANGE = -1
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#
# class Promoted_Bishop:  # can be renamed to "Uma" or "Horse"
#     MOVEMENT = Bishop.MOVEMENT
#     MOVEMENT_RANGE = -1
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)


if __name__ == '__main__':
    pieces = [Pawn, Knight, Bishop, Rook, Queen, King,
              S_Pawn, Lance, S_Knight, Silver, Gold]
    for piece in pieces:
        print(piece.name(), end="\n\t")
        print(*piece.MOVEMENT, sep="\n\t", end="\n\t")
        print("Range: ", piece.MOVEMENT_RANGE)

    print("*" * 50)
    rook = Rook(x=5, y=5)
    for vector in rook.get_possible_moves(board_size=8):
        print(vector)
