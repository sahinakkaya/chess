import unittest
from chessVshogi.directions import Direction, Vector2D, SetOfVectors


class DirectionTestCase(unittest.TestCase):
    def setUp(self):
        self.bishops_dir = Direction.LDIAGONAL | Direction.RDIAGONAL
        self.rooks_dir = Direction.HORIZONTAL | Direction.VERTICAL
        self.queens_dir = self.bishops_dir | self.rooks_dir

    def test_single_dir(self):
        self.assertEqual((-1, 0), Direction.LEFT)
        self.assertEqual((0, 1), Direction.FORWARD)

    def test_multiple_dir_normal_cases(self):
        self.assertEqual({(-1, 0), (1, 0)}, Direction.HORIZONTAL)
        self.assertEqual({(0, 1), (0, -1)}, Direction.VERTICAL)
        self.assertEqual({(-1, 1), }, Direction.FORWARD & Direction.LEFT)
        self.assertEqual({(1, -1), }, Direction.RIGHT & Direction.BACKWARD)
        self.assertEqual({(-1, 1), (1, -1)}, Direction.LDIAGONAL)

    def test_multiple_dir_extreme_cases(self):
        self.assertEqual({(0, -1), (-1, 0), (1, 0)},
                         Direction.BACKWARD | Direction.HORIZONTAL)
        self.assertEqual(set(), Direction.BACKWARD & Direction.FORWARD)
        self.assertEqual({(-1, 1), (1, 1)},
                         Direction.HORIZONTAL & Direction.FORWARD)

    def test_reversed_container(self):
        self.assertEqual(Direction.RIGHT, reversed(Direction.LEFT))
        self.assertEqual(Direction.LDIAGONAL, reversed(Direction.LDIAGONAL))

    def test_flip_horizontal_and_vertical(self):
        self.assertEqual(Direction.LEFT, Direction.RIGHT.flip("h"))
        self.assertEqual(Direction.RIGHT, Direction.RIGHT.flip("v"))
        self.assertEqual(Direction.FORWARD, Direction.FORWARD.flip("h"))
        self.assertEqual(Direction.BACKWARD, Direction.FORWARD.flip("v"))
        self.assertEqual(Direction.LDIAGONAL, Direction.RDIAGONAL.flip("h"))

    def test_multiple_flips(self):
        self.assertEqual(Direction.LEFT, Direction.LEFT.flip().flip())
        self.assertEqual(Direction.LEFT, Direction.RIGHT.flip("v").flip("h"))
        self.assertEqual(self.queens_dir, self.queens_dir.flip("v"))
        self.assertEqual(self.queens_dir, self.queens_dir.flip().flip().flip())
        self.assertEqual(self.bishops_dir,
                         self.bishops_dir.flip("v").flip("h"))

    def test_flip_raises_error_when_wrong_parameter_specified(self):
        self.assertRaises(ValueError, Direction.LDIAGONAL.flip, "a")

    def test_flip_affects_the_caller(self):
        left = Vector2D(-1, 0)
        left.flip("h", True)
        self.assertEqual(Direction.RIGHT, left)
        knight = SetOfVectors((1, 2), (2, 1))
        knight.flip("v", True).flip("h", True)
        self.assertTrue(SetOfVectors((-2, -1), (1, -2)).issubset(knight))

    def test_chess_pieces(self):
        self.assertEqual({(-1, 1), (1, -1), (-1, -1), (1, 1)},
                         self.bishops_dir)
        self.assertEqual({(-1, 0), (1, 0), (0, 1), (0, -1)}, self.rooks_dir)
        self.assertTrue(self.bishops_dir.issubset(self.queens_dir))
        self.assertTrue(self.rooks_dir.issubset(self.queens_dir))
        self.assertEqual(self.queens_dir,
                         self.rooks_dir.union(self.bishops_dir))


if __name__ == '__main__':
    unittest.main()
