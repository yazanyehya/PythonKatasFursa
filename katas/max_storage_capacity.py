from typing import List


def max_storage_area(containers: List[int]) -> int:
    containers.append(0)
    stack = []
    max_area = 0

    for i in range(len(containers)):
        while stack and containers[i] <= containers[stack[-1]]:
            height = containers[stack.pop()]
            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1
            area = height * width
            max_area = max(max_area, area)

        stack.append(i)
    return max_area


if __name__ == "__main__":
    containers = [2, 1, 5, 6, 2, 3]
    result = max_storage_area(containers)
    print("Max storage area:", result)  # Expected output: 10
