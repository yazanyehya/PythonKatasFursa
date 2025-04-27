import unittest
from katas.reduce_list import reduce_array

class TestReduceArray(unittest.TestCase):
    def test_normal_case(self):
        numbers = [10,15,7,20,25]
        reduce_array(numbers)
        self.assertEqual(numbers,[10,5,-8,13,5])

    def test_single_element(self):
        numbers=[5]
        reduce_array(numbers)
        self.assertEqual(numbers,[5])

    def test_empty_list(self):
        numbers = []
        reduce_array(numbers)
        self.assertEqual(numbers,[])

    def test_all_zeros(self):
        numbers = [0,0,0,0]
        reduce_array(numbers)
        self.assertEqual(numbers,[0,0,0,0])

    def test_negative_numbers(self):
        numbers = [-5,-10,-15,-20]
        reduce_array(numbers)
        self.assertEqual(numbers,[-5,-5,-5,-5])

    def test_positive_negative_numbers(self):
        numbers = [10,-5,20,-10]
        reduce_array(numbers)
        self.assertEqual(numbers,[10,-15,25,-30])


if __name__ == "main":
    unittest.main()



