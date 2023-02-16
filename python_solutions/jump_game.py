from typing import List


def canJump(nums: List[int]) -> bool:
    if len(nums) == 1:
        return True

    target_idx = len(nums) - 1
    interval = (0, nums[0])
    for i in range(1, len(nums)):
        if (interval[1] >= i) and (interval[1] < i + nums[i]):
            interval = (0, i + nums[i])
            if interval[1] >= target_idx:
                return True
    return interval[1] >= target_idx


if __name__ == '__main__':
    test_cases = [
        {'input': [0], 'output': True},
        {'input': [2, 0], 'output': True},
        {'input': [2,3,1,1,4], 'output': True},
        {'input': [3,2,1,0,4], 'output': False}
    ]
    for test_case in test_cases:
        ans = canJump(test_case['input'])
        assert ans == test_case['output']
