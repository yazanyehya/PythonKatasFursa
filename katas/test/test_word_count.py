import unittest
from katas.word_count import count_words

class TestIsUniqueStr(unittest.TestCase):
    def test_normal_sentence(self):
        self.assertEqual(count_words("This is a sample sentence for counting words."),8)

    def test_empty_string(self):
        self.assertEqual(count_words(""),0)

    def test_only_spaces(self):
        self.assertEqual(count_words("              "),0)

    def test_single_word(self):
        self.assertEqual(count_words("yazan"),1)

    def test_multiple_spaces_between_word(self):
        self.assertEqual(count_words("This is    a sample sentence      for                 counting words."),8)

    def test_words_with_numbers_and_symbols(self):
        self.assertEqual(count_words("Python3 is fun! Right?"),4)


if __name__ == "main":
    unittest.main()