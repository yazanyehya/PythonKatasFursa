import  unittest
from katas.true_counter import count_true_values

class TestTrueCounter(unittest.TestCase):
    def test_mixed_values(self):
        array = [True, False, True, True, False]
        self.assertEqual(count_true_values(array), 3)

    def test_all_true(self):
        array = [True, True, True, True, True]
        self.assertEqual(count_true_values(array), 5)

    def test_all_false(self):
        array = [False, False, False, False, False]
        self.assertEqual(count_true_values(array), 0)

    def test_empty_list(self):
        array = []
        self.assertEqual(count_true_values(array),0)

    def test_single_true(self):
        array = [True]
        self.assertEqual(count_true_values(array),1)

    def test_single_false(self):
        array = [False]
        self.assertEqual(count_true_values(array),0)


if __name__ == "main":
    unittest.main()