from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    num_to_idx = {}
    pairs = []
    for idx, el in enumerate(nums):
        if target - el not in num_to_idx:
            num_to_idx[el] = idx
        else:
            pairs.append((target - el, el))
            num_to_idx[target - el] = idx
    return pairs


def threeSum(nums: List[int]) -> List[List[int]]:
    # Time complexity: O(N) * O(N) = O(N^2)
    # Space complexity: O(N)
    triplets = set()
    for idx, el in enumerate(nums[:-2]):
        pairs = twoSum(nums[idx + 1:], -el)
        if not pairs:
            continue
        for (el2, el3) in pairs:
            triplet = tuple(sorted([el, el2, el3]))
            triplets.add(triplet)
    return [list(triplet) for triplet in triplets]


if __name__ == '__main__':
    test_cases = [
        {'input': [0,1,1], 'output': []},
        {'input': [-1,0,1,2,-1,-4], 'output': [[-1,-1,2],[-1,0,1]]},
        {'input': [0,0,0], 'output': [[0,0,0]]},
    ]

    for test_case in test_cases:
        ans = threeSum(test_case['input'])
        print(ans == test_case['output'], ans)