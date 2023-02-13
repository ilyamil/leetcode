import enum
from typing import List


def maxSubArray(nums: List[int]) -> int:
    dp = nums
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
    return max(dp)


if __name__ == '__main__':
    test_cases = [
        {'input': [-2,1,-3,4,-1,2,1,-5,4], 'output': 6},
        {'input': [1], 'output': 1},
        {'input': [5,4,-1,7,8], 'output': 23},
        {'input': [-1,1,-1,1,-1,2,-1,3,-2,-1], 'output': 4}
    ]
    for test_case in test_cases:
        ans = maxSubArray(test_case['input'])
        print(ans, ans == test_case['output'])
