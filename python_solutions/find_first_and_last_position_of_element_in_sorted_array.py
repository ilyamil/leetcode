from typing import List


def lower_bound(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if (nums[mid] >= target):
            right = mid
        else:
            left = mid + 1
    return left


def searchRange(nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1, -1]

    left = lower_bound(nums, target)
    if nums[left] != target:
        left = -1
        right = -1
    else:
        right = lower_bound(nums, target + 1)
        if nums[right] != target:
            right -= 1
    return [left, right]


if __name__ == '__main__':
    test_cases = [
        {'nums': [5,7,7,8,8,10], 'target': 8, 'output': [3,4]},
        {'nums': [5,7,7,8,8,10], 'target': 6, 'output': [-1,-1]},
        {'nums': [4,5,6,7,8,9], 'target': 4, 'output': [0,0]},
        {'nums': [4,5,6,7,8,9], 'target': 9, 'output': [5, 5]},
        {'nums': [4,5,6,7,9,9], 'target': 9, 'output': [4, 5]},
        {'nums': [1], 'target': 0, 'output': [-1,-1]},
        {'nums': [], 'target': 0, 'output': [-1, -1]},
    ]
    # arr = [4,5,6,7,8,9,10,11]
    # target = 11
    # print(binsearch(arr, 0, len(arr) - 1, target))

    for test_case in test_cases:
        # ans = lower_bound(test_case['nums'], test_case['target'])
        ans = searchRange(test_case['nums'], test_case['target'])
        print(ans, ans == test_case['output'])