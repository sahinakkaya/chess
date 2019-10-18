import itertools


class Vector2D:
    """
    A vector that represents a direction in 2D space
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y

    def __or__(self, other):
        if isinstance(other, Vector2D):
            return SetOfVectors(self) | SetOfVectors(other)
        elif isinstance(other, SetOfVectors):
            return other | self
        return NotImplemented

    def __and__(self, other):
        if isinstance(other, Vector2D):
            other = SetOfVectors(other)
        if isinstance(other, SetOfVectors):
            return SetOfVectors(self) & other
        return NotImplemented

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            other = Vector2D(*other)
        if isinstance(other, SetOfVectors):
            return other == SetOfVectors(self)
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __hash__(self):
        return hash((str(self)))

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector2D(self.x * other, self.y * other)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            other = Vector2D(*other)
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented


class SetOfVectors(set):
    """
    A class used to store Vector2D objects in a set

    Takes unknown amount of "pair"s and converts them
    to Vector2D objects implicitly

    pair is an iterable that consists of 2 elements
    """

    def __init__(self, *args):
        new_args = []
        for arg in args:
            new_args.append(self.convert_pair_to_vector(arg))
        super().__init__(new_args)

    @staticmethod
    def convert_pair_to_vector(p):
        try:
            return Vector2D(*p)
        except TypeError:
            raise TypeError(f"pairs should have exactly 2 elements: {p}")

    def __or__(self, other):
        return_val = self.copy()
        if isinstance(other, Vector2D):
            return_val.add(other)
        elif isinstance(other, SetOfVectors):
            return_val.update(other)
        else:
            return NotImplemented
        return SetOfVectors(*return_val)

    def __and__(self, other):
        if isinstance(other, Vector2D):
            other = SetOfVectors(other)
        if isinstance(other, SetOfVectors):
            pairs = SetOfVectors()
            for pair1, pair2 in itertools.combinations(self | other, 2):
                pair = pair1 + pair2
                if pair != Vector2D(0, 0):
                    pairs.add(pair)
            return pairs
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, set):
            other = SetOfVectors(*other)
        return super().__eq__(other)


class Direction:
    """
    A class that defines directions in 2D space as Vectors
    """
    LEFT = Vector2D(-1, 0)
    RIGHT = Vector2D(1, 0)
    FORWARD = Vector2D(0, 1)
    BACKWARD = Vector2D(0, -1)
    HORIZONTAL = LEFT | RIGHT
    VERTICAL = FORWARD | BACKWARD
    LDIAGONAL = (LEFT & FORWARD) | (RIGHT & BACKWARD)
    RDIAGONAL = (LEFT & BACKWARD) | (RIGHT & FORWARD)
