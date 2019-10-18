import unittest
from chessVshogi.directions import Direction


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

    def test_chess_pieces(self):
        self.assertEqual({(-1, 1), (1, -1), (-1, -1), (1, 1)},
                         self.bishops_dir)
        self.assertEqual({(-1, 0), (1, 0), (0, 1), (0, -1)}, self.rooks_dir)
        self.assertTrue(self.bishops_dir.issubset(self.queens_dir))
        self.assertTrue(self.rooks_dir.issubset(self.queens_dir))
        self.assertEqual(self.queens_dir,
                         self.rooks_dir.union(self.bishops_dir))

    def test_reversed_container(self):
        self.assertEqual(Direction.RIGHT, reversed(Direction.LEFT))
        self.assertEqual(Direction.LDIAGONAL, reversed(Direction.LDIAGONAL))


if __name__ == '__main__':
    unittest.main()
