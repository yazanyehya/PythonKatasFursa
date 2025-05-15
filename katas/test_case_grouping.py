from typing import List
from collections import defaultdict


def group_test_cases(test_case_group_sizes: List[int]) -> List[List[int]]:

    result = []
    size_to_indices = defaultdict(list)

    for index, group_size in enumerate(test_case_group_sizes):
        size_to_indices[group_size].append(index)

        if len(size_to_indices[group_size]) == group_size:
            result.append(size_to_indices[group_size])
            size_to_indices[group_size] = []  # reset the group

    return result



if __name__ == '__main__':
    # Example 1
    test_case_group_sizes1 = [1, 2, 3, 3, 3, 2]
    result1 = group_test_cases(test_case_group_sizes1)
    print(f"Input: {test_case_group_sizes1}")
    print(f"Output: {result1}")  # Expected: something like [[0], [1, 5], [2, 3, 4]]

    # Verification
    if result1:
        valid = True
        covered_indices = []

        for group in result1:
            # Check if all elements in this group require same group size
            expected_size = test_case_group_sizes1[group[0]]
            if not all(test_case_group_sizes1[idx] == expected_size for idx in group):
                valid = False
                print("Invalid: Not all test cases in a group require the same group size")
                break

            # Check if group size matches the required size
            if len(group) != expected_size:
                valid = False
                print(f"Invalid: Group {group} has size {len(group)} but should have size {expected_size}")
                break

            covered_indices.extend(group)

        # Check if all test cases are covered exactly once
        if sorted(covered_indices) != list(range(len(test_case_group_sizes1))):
            valid = False
            print("Invalid: Not all test cases are covered exactly once")

        print(f"Solution is valid: {valid}")

    # Example 2 - simpler case
    test_case_group_sizes2 = [2, 2, 1, 1]
    result2 = group_test_cases(test_case_group_sizes2)
    print(f"\nInput: {test_case_group_sizes2}")
    print(f"Output: {result2}")  # Expected: something like [[0, 1], [2], [3]]