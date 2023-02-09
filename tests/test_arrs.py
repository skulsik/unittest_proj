from utils import arrs
import unittest


class Test_arrs(unittest.TestCase):
    def test_get_1(self):
        self.assertEqual(arrs.get([1, 2, 3], -2), None)

    def test_get_2(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)

    def test_get_3(self):
        self.assertEqual(arrs.get([], 0, "test"), "test")


    def test_slice_1(self):
        self.assertEqual(arrs.my_slice([]), [])


    def test_slice_2(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], 1, 2), [2])


    def test_slice_3(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -6, 3), [1, 2, 3])


    def test_slice_4(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], -1), [3])


    def test_slice_5(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], -1, -5), [])
