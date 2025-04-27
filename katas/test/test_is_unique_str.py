import unittest
from katas.is_unique_str import is_unique

class TestIsUniqueStr(unittest.TestCase):
    def test_duplicate_letters(self):
        self.assertFalse(is_unique("yazan"))

    def test_all_unique_letters(self):
        self.assertTrue(is_unique("world"))

    def test_empty_word(self):
        self.assertTrue(is_unique(""))

    def test_single_letter(self):
        self.assertTrue(is_unique("N"))

    def test_case_sensitive_unique(self):
        self.assertTrue(is_unique("Yehya"))

    def test_case_sensitive_duplicate(self):
        self.assertFalse(is_unique("yehya"))


if __name__ == "main":
    unittest.main()