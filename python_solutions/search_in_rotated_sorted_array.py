from typing import List


def binsearch(arr: List[int], left: int, right: int, target: int) -> int:
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def search(nums: List[int], target: int) -> int:
    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    left = 0
    right = len(nums) - 1
    pivot = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if (mid >= 1) and (nums[mid - 1] > nums[mid]):
            pivot = mid
            break
        # check if we are in a left subarray
        if nums[mid] > nums[-1]:
            left = mid + 1
        else:
            right = mid - 1
    # the array is not rotated
    if pivot == -1:
        return binsearch(nums, 0, len(nums) - 1, target)
    if target > nums[-1]:
        return binsearch(nums, 0, pivot, target)
    if target < nums[0]:
        return binsearch(nums, pivot, len(nums) - 1, target)
    if target == nums[-1]:
        return len(nums) - 1
    if target == nums[0]:
        return 0
    return pivot


if __name__ == '__main__':
    test_cases = [
        {'nums': [4,5,6,7,0,1,2], 'target': 0, 'output': 4},
        {'nums': [4,5,6,7,0,1,2], 'target': 3, 'output': -1},
        {'nums': [4,5,6,7,8,9,2], 'target': 3, 'output': -1},
        {'nums': [4,5,6,7,8,9,10], 'target': 4, 'output': 0},
        {'nums': [7,0,1,2,3,4,5], 'target': 5, 'output': 6},
        {'nums': [7,8,0,1,2,3,4,5], 'target': 8, 'output': 1},
        {'nums': [1], 'target': 0, 'output': -1},
    ]
    # arr = [4,5,6,7,8,9,10,11]
    # target = 11
    # print(binsearch(arr, 0, len(arr) - 1, target))

    for test_case in test_cases:
        ans = search(test_case['nums'], test_case['target'])
        print(ans, ans == test_case['output'])
