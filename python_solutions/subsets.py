from typing import List


def backtrack(nums, subs, cur_subset, start):
    subs.append([s for s in cur_subset])

    for i in range(start, len(nums)):
        cur_subset.append(nums[i])
        backtrack(nums, subs, cur_subset, i + 1)
        cur_subset.pop()


def subsets(nums: List[int]) -> List[List[int]]:
    subs = []
    backtrack(nums, subs, [], 0)
    return subs


if __name__ == '__main__':
    test_cases = [
        {'input': [1,2,3], 'output': [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]},
        # {'input': [0], 'output': [[],[0]]}
    ]
    for test_case in test_cases:
        nums = test_case['input']
        subs = subsets(nums)
        print(subs)
