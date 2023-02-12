from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    num_to_idx = {}
    for idx, el in enumerate(nums):
        if target - el not in num_to_idx:
            num_to_idx[el] = idx
        else:
            return [num_to_idx[target - el], idx]
    return [-1, -1]


if __name__ == '__main__':
    test_cases = [
        {'nums': [2,7,11,15], 'target': 9, 'output': [0, 1]},
        {'nums': [3,2,4], 'target': 6, 'output': [1, 2]},
        {'nums': [3,3], 'target': 6, 'output': [0, 1]},
    ]

    for test_case in test_cases:
        answer = twoSum(test_case['nums'], test_case['target'])
        print(answer == test_case['output'])
