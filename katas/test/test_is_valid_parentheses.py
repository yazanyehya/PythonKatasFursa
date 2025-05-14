import unittest
from katas.is_valid_parentheses import is_valid_parentheses

class TestValidParentheses(unittest.TestCase):
    def test_valid_parentheses(self):
        self.assertTrue(is_valid_parentheses("()"))
        self.assertTrue(is_valid_parentheses("[]"))
        self.assertTrue(is_valid_parentheses("{}"))
        self.assertTrue(is_valid_parentheses("()[]{}"))
        self.assertTrue(is_valid_parentheses("{[]()}"))
        self.assertTrue(is_valid_parentheses(""))
        self.assertTrue(is_valid_parentheses("({[]})"))
    def test_invalid_parentheses(self):
        self.assertFalse(is_valid_parentheses("("))
        self.assertFalse(is_valid_parentheses("]"))
        self.assertFalse(is_valid_parentheses("([)]"))
        self.assertFalse(is_valid_parentheses("({[)]}"))
        self.assertFalse(is_valid_parentheses("(()"))
        self.assertFalse(is_valid_parentheses("((()))]"))


if __name__ =='__main__':
    unittest.main()