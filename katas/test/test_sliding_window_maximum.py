import unittest
from katas.sliding_window_maximum import max_sliding_window  # Replace 'your_module' with the filename (no .py)

class TestMaxSlidingWindow(unittest.TestCase):

    def test_example_case(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [3, 3, 5, 5, 6, 7]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_two_elements_window(self):
        nums = [9, 11, 3, 4, 8, 7]
        k = 2
        expected = [11, 11, 4, 8, 8]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_window_size_one(self):
        nums = [1, -1]
        k = 1
        expected = [1, -1]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_window_equals_array(self):
        nums = [4, 2, 12]
        k = 3
        expected = [12]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_all_same_elements(self):
        nums = [5, 5, 5, 5]
        k = 2
        expected = [5, 5, 5]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_single_element_array(self):
        nums = [10]
        k = 1
        expected = [10]
        self.assertEqual(max_sliding_window(nums, k), expected)

    def test_invalid_window_size(self):
        nums = [1, 2, 3]
        k = 0
        with self.assertRaises(ValueError):
            max_sliding_window(nums, k)

if __name__ == '__main__':
    unittest.main()
