import unittest
from typing import List
from katas.test_case_grouping import group_test_cases

class TestGroupTestCases(unittest.TestCase):

    def validate_grouping(self, input_sizes: List[int], result: List[List[int]]):


        flat = [i for group in result for i in group]
        self.assertCountEqual(flat, list(range(len(input_sizes))))

        for group in result:
            expected_size = input_sizes[group[0]]
            for i in group:
                self.assertEqual(input_sizes[i], expected_size)
            self.assertEqual(len(group), expected_size)

    def test_example1(self):
        input_sizes = [1, 2, 3, 3, 3, 2]
        result = group_test_cases(input_sizes)
        self.validate_grouping(input_sizes, result)

    def test_example2(self):
        input_sizes = [2, 2, 1, 1]
        result = group_test_cases(input_sizes)
        self.validate_grouping(input_sizes, result)

    def test_all_single(self):
        input_sizes = [1, 1, 1]
        result = group_test_cases(input_sizes)
        self.validate_grouping(input_sizes, result)

    def test_all_same_large_group(self):
        input_sizes = [3, 3, 3, 3, 3, 3]
        result = group_test_cases(input_sizes)
        self.validate_grouping(input_sizes, result)

    def test_invalid_group_size(self):
        # Incomplete group should not happen based on problem statement,
        # but we'll simulate one for testing if function fails gracefully.
        input_sizes = [2, 2, 2]
        result = group_test_cases(input_sizes)
        total_grouped = sum(len(group) for group in result)
        self.assertNotEqual(total_grouped, 3)  # Not enough to form two groups of 2


if __name__ == '__main__':
    unittest.main()
