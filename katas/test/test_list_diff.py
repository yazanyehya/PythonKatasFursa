import unittest
from katas.list_diff import find_difference

class TestFindDiff(unittest.TestCase):
    def test_positive_numbers(self):
        numbers = [10,3,5,6,20,2]
        self.assertEqual(find_difference(numbers),18)

    def test_shuffle_numbers(self):
        numbers = [10,3,5,6,20,-2]
        self.assertEqual(find_difference(numbers),22)

    def test_single_element(self):
        numbers = [10]
        self.assertEqual(find_difference(numbers),0)

    def test_negative_numbers(self):
        numbers = [-10,-20,-5,-15]
        self.assertEqual(find_difference(numbers),15)

    def test_empty_list(self):
        numbers = []
        with self.assertRaises(ValueError):
            find_difference(numbers)

if __name__ == "main":
    unittest.main()