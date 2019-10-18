from chessVshogi.directions import Direction, SetOfVectors


class Piece:
    """
    Base class for a piece in the game
    """
    MOVEMENT = SetOfVectors()
    MOVEMENT_RANGE = 1

    def __init__(self, x, y, promotable=False,
                 has_promoted=False,
                 is_dead=False):
        self.x = x
        self.y = y
        self.promotable = promotable
        self.has_promoted = has_promoted
        self.is_dead = is_dead

    @classmethod
    def name(cls):
        return cls.__name__


class ChessPiece(Piece):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ShogiPiece(Piece):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Pawn(ChessPiece):
    MOVEMENT = Direction.FORWARD | (
            Direction.HORIZONTAL & Direction.FORWARD)
    MOVEMENT_RANGE = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Knight(ChessPiece):
    MOVEMENT = SetOfVectors((2, 1), (1, 2)).flip(
        axes="h", in_place=True).flip(axes="v", in_place=True)
    MOVEMENT_RANGE = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Rook(ChessPiece):
    MOVEMENT = Direction.HORIZONTAL | Direction.VERTICAL
    MOVEMENT_RANGE = 8

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Bishop(ChessPiece):
    MOVEMENT = Direction.LDIAGONAL | Direction.RDIAGONAL
    MOVEMENT_RANGE = 8

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Queen(ChessPiece):
    MOVEMENT = Rook.MOVEMENT | Bishop.MOVEMENT
    MOVEMENT_RANGE = 8

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class King(ChessPiece):
    MOVEMENT = Queen.MOVEMENT
    MOVEMENT_RANGE = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


if __name__ == '__main__':
    pieces = [Pawn, Knight, Bishop, Rook, Queen, King]
    for piece in pieces:
        print(piece.name(), end="\n\t")
        print(*piece.MOVEMENT, sep="\n\t", end="\n\t")
        print("Range: ", piece.MOVEMENT_RANGE)
