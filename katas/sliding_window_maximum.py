import collections

from debian.debtags import output


def max_sliding_window(nums, k):
    # slide = []
    # j = k
    # answer = []
    # for i in range(len(nums)):
    #     if j > 0 :
    #         slide.append(nums[i])
    #         j-=1
    #     else :
    #         answer.append(max(slide))
    #         slide.append(nums[i])
    #         slide.pop(0)
    #
    # answer.append(max(slide))
    #
    # return answer
    if k <= 0 or k > len(nums):
        raise ValueError("Window size k must be between 1 and len(nums)")
    answer = []
    q = collections.deque()
    l = 0

    for r in range(len(nums)):
        # Remove from back if smaller than current
        while q and nums[q[-1]] < nums[r]:
            q.pop()

        q.append(r)

        # Remove from front if out of window
        if q[0] < l:
            q.popleft()

        # Record result when window is valid
        if r - l + 1 >= k:
            answer.append(nums[q[0]])
            l += 1

    return answer


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    result = max_sliding_window(nums, k)
    print(f"Sliding window maximums: {result}")  # Expected: [3, 3, 5, 5, 6, 7]

    # Additional test cases
    nums2 = [9, 11, 3, 4, 8, 7]
    k2 = 2
    result2 = max_sliding_window(nums2, k2)
    print(f"Sliding window maximums: {result2}")  # Expected: [11, 11, 4, 8, 8]

    nums3 = [1, -1]
    k3 = 1
    result3 = max_sliding_window(nums3, k3)
    print(f"Sliding window maximums: {result3}")  # Expected: [1, -1]