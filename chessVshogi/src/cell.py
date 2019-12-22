class Cell:
    def __init__(self, x, y, piece=None):
        self.x = x
        self.y = y
        self.piece = piece
        self.shadow = None

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.piece

    def __repr__(self):
        if self.piece:
            return f"{self.piece.name_}"
        elif self.shadow:
            return f"{self.shadow.x} {self.shadow.y}"
        else:
            return f"    "

    def clear(self):
        self.piece = None

    def set_piece(self, piece):
        if self.shadow is not None:
            if piece.name() == "Pawn":
                self.shadow.clear()
            self.shadow = None

        self.clear()
        self.piece = piece
        previous_pos = self.piece.x, self.piece.y
        self.piece.set_position(self.x, self.y)
        piece = self.piece
        if piece.promotable:
            if (piece.side == "W" and piece.y >= piece.promoting_rank) or \
                    (piece.side == "B" and piece.y <= piece.promoting_rank):
                piece.promote_trigger()
            else:  # this segment will be required later.
                prev_y = previous_pos[1]
                if (piece.side == "W" and prev_y >= piece.promoting_rank) or \
                        (piece.side == "B" and prev_y <= piece.promoting_rank):
                    piece.promote_trigger()