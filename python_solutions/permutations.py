from itertools import permutations
from typing import List


def backtrack(permutations, visited, nums, cur):
    if len(cur) == len(nums):
        permutations.append(cur)

    for i in range(len(nums)):
        if i not in visited:
            visited.add(i)
            backtrack(permutations, visited, nums, cur + [nums[i]])
            visited.remove(i)


def permute(nums: List[int]) -> List[List[int]]:
    permutations = []
    visited = set()
    backtrack(permutations, visited, nums, [])
    return permutations


if __name__ == '__main__':
    test_cases = [
        {'input': [1,2,3], 'output': [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]},
        {'input': [0,1], 'output': [[0,1],[1,0]]},
        {'input': [1], 'output': [[1]]}
    ]
    for test_case in test_cases:
        ans = permute(test_case['input'])
        print(ans)