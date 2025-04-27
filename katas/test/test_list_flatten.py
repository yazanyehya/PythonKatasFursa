import unittest
from katas.list_flatten import flatten_list

class TestFlattenList(unittest.TestCase):
    def test_flat_list(self):
        self.assertEqual(flatten_list([1,2,3]),[1,2,3])

    def test_one_level_nesting(self):
        self.assertEqual(flatten_list([1,[2,3],4]),[1,2,3,4])

    def test_deep_nesting(self):
        self.assertEqual(flatten_list([1,[2,[3,4]],5]),[1,2,3,4,5])

    def test_empty_list(self):
        self.assertEqual(flatten_list([]),[])

    def test_mixed_types(self):
        self.assertEqual(flatten_list([1,['a','b'],2,'hello']),[1,'a','b',2,'hello'])

    def test_many_empty_lists(self):
        self.assertEqual(flatten_list([[],[],[]]),[])


if __name__ == "main":
    unittest.main()
