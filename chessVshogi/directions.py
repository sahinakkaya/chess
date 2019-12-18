import itertools
from functools import partial, wraps


def convert_tuple_to_vector(function):
    @wraps(function)
    def wrapper(first, second):
        if isinstance(first, tuple) and len(first) == 2:
            first = Vector2D(*first)
        if isinstance(second, tuple) and len(second) == 2:
            second = Vector2D(*second)
        return function(first, second)

    return wrapper


def return_not_implemented_if_not_vector(function):
    @wraps(function)
    def wrapper(first, second):
        if not isinstance(second, Vector2D):
            return NotImplemented
        return function(first, second)

    return wrapper


def handle_non_vector_params(function):
    @convert_tuple_to_vector
    @return_not_implemented_if_not_vector
    @wraps(function)
    def wrapper(first, second):
        return function(first, second)

    return wrapper


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

    @handle_non_vector_params
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    @handle_non_vector_params
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    @handle_non_vector_params
    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    @handle_non_vector_params
    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    @convert_tuple_to_vector
    def __eq__(self, other):
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

    def __reversed__(self):
        return self * -1

    @handle_non_vector_params
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def flip(self, axes=None, in_place=False):
        """
        Return an instance of Vector2D that is flipped against 'axes'

        :param axes: a parameter that can be "horizontal", "vertical" or None
        :param in_place: if True the result will be set to the caller
        :return: a Vector2D instance that is flipped against 'axes'
        """
        result = SetOfVectors(self).flip(axes, False).pop()
        if in_place:
            self.x, self.y = result
        return result


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

    def __contains__(self, item):
        for x, y in self:
            if (x, y) == item:
                return True
        else:
            return False

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

    def __mul__(self, other):
        if isinstance(other, int):
            return SetOfVectors(*(vector * other for vector in self))
        return NotImplemented

    def __reversed__(self):
        return self * -1

    def __eq__(self, other):
        if isinstance(other, set):
            other = SetOfVectors(*other)
        return super().__eq__(other)

    @staticmethod
    def change_sign_of_value_at_index(t: tuple, index: int):
        return tuple(data
                     if i != index
                     else -data
                     for i, data in enumerate(t))

    def flip(self, axes=None, in_place=False):
        """
        Flip all the elements horizontally, vertically or against origin and
        return them

        :param axes: a parameter that can be "horizontal", "vertical" or None
        :param in_place: if True the result will be used to update the caller
        :return: SetOfVectors that is flipped against 'axes'
        """
        if in_place:
            self.update(self.flip(axes))
            return self
        if axes is None:
            return reversed(self)
        else:
            if axes in ("horizontal", "h"):
                index = 0
            elif axes in ("vertical", "v"):
                index = 1
            else:
                raise ValueError(
                    "axes value should be 'horizontal' or 'vertical' when set")
            mapping_func = partial(self.change_sign_of_value_at_index,
                                   index=index)
            return SetOfVectors(*map(mapping_func, self))


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
    STRAIGHT = VERTICAL | HORIZONTAL
    DIAGONAL = LDIAGONAL | RDIAGONAL
