import unittest
import main
class TestQuickSort(unittest.TestCase):
    def test_1(self):
        expected = [0, 1, 2, 3, 5]
        x = main.Array([2, 1, 5, 3, 0]).QuickSort(0, len([2, 1, 5, 3, 0])-1)
        self.assertEqual(expected, x)
    def test_2(self):
        expected = []
        x = main.Array([]).QuickSort(0, len([]) - 1)
        self.assertEqual(expected, x)
    def test_3(self):
        expected = [0, 1, 1, 2, 4, 6]
        x = main.Array([2, 1, 4, 6, 1, 0]).QuickSort(0, len([2, 1, 4, 6, 1, 0]) - 1)
        self.assertEqual(expected, x)
    def test_4(self):
        expected = [0, 0, 0, 0, 0, 0]
        x = main.Array([0, 0, 0, 0, 0, 0]).QuickSort(0, len([0, 0, 0, 0, 0, 0]) - 1)
        self.assertEqual(expected, x)
    def test_5(self):
        expected = [0.25, 1/3, 2, 2.33, 10.566, 45.0]
        x = main.Array([0.25, 10.566, 2.33, 1/3, 45.0, 2]).QuickSort(0, len([0.25, 10.566, 2.33, 1/3, 45.0, 2]) - 1)
        self.assertEqual(expected, x)
    def test_6(self):
        with self.assertRaises(TypeError):
            x = main.Array([0.25, 10.566, "2.33", 1/3, 45.0, 2]).QuickSort(0, len([0.25, 10.566, "2.33", 1/3, 45.0, 2]) - 1)
