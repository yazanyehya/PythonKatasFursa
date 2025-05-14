import unittest
from katas.max_storage_capacity import max_storage_area

class TestMaxStorageArea(unittest.TestCase):

    def test_general_case(self):
        self.assertEqual(max_storage_area([2, 1, 5, 6, 2, 3]), 10)

    def test_single_bar(self):
        self.assertEqual(max_storage_area([4]), 4)

    def test_increasing_heights(self):
        self.assertEqual(max_storage_area([1, 2, 3, 4, 5]), 9)  # 3*3 = 9

    def test_decreasing_heights(self):
        self.assertEqual(max_storage_area([5, 4, 3, 2, 1]), 9)  # 3*3 = 9

    def test_all_equal_heights(self):
        self.assertEqual(max_storage_area([3, 3, 3, 3]), 12)  # 4*3 = 12

    def test_empty_list(self):
        self.assertEqual(max_storage_area([]), 0)

    def test_plateau_case(self):
        self.assertEqual(max_storage_area([2, 4, 2, 1]), 6)  # 2 at index 0 to index 2 => 2*3 = 6

if __name__ == '__main__':
    unittest.main()
