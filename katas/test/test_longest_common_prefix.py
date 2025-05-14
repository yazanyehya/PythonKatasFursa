import unittest
from katas.longest_common_prefix import longest_common_prefix

class TestLongestCommonPrefix(unittest.TestCase):
    def test_regular_cases(self):
        test1 = ["flower", "flow", "flight"]
        test3 = ["interspecies", "interstellar", "interstate"]
        test4 = ["apple", "apricot", "ape"]
        self.assertEqual(longest_common_prefix(test1),"fl")
        self.assertEqual(longest_common_prefix(test3),"inters")
        self.assertEqual(longest_common_prefix(test4),"ap")

    def test_no_common_prefix(self):
        test2 = ["dog", "racecar", "car"]
        self.assertEqual(longest_common_prefix(test2),"")

    def test_single_string(self):
        self.assertEqual(longest_common_prefix(["single"]),"single")

    def test_empty_list(self):
        self.assertEqual(longest_common_prefix([]), "")

    def test_list_with_empty_string(self):
        self.assertEqual(longest_common_prefix(["", "prefix", "pre"]), "")

    def test_all_same_string(self):
        self.assertEqual(longest_common_prefix(["same", "same", "same"]), "same")

if __name__ == '__main__':
    unittest.main()



