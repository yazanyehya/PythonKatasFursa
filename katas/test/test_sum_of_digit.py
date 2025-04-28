import unittest
from katas.sum_of_digits import sum_of_digits

class TestSumOfDigit(unittest.TestCase):
    def test_digits_in_string(self):
        self.assertEqual(sum_of_digits("abcd123"),6)

    def test_digits_with_text(self):
        self.assertEqual(sum_of_digits("i left 100 kg in bench press ,12 reps"),4)

    def test_no_digits(self):
        self.assertEqual(sum_of_digits("i love to go to the gym"),0)

    def test_only_digits(self):
        self.assertEqual(sum_of_digits("123456"),21)

    def test_empty_string(self):
        self.assertEqual(sum_of_digits(""),0)

if __name__ == "main":
    unittest.main()
