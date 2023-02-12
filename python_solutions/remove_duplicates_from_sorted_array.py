import enum
from typing import List


def removeDuplicates(nums: List[int]) -> int:
    seen_elements = {nums[0]}
    last_idx = 1
    for idx, el in enumerate(nums):
        if idx == 0 or el in seen_elements:
            continue
        seen_elements.add(el)
        print(last_idx, idx)
        nums[last_idx], nums[idx] = nums[idx], nums[last_idx]
        last_idx += 1
    return last_idx


if __name__ == '__main__':
    # nums = [1,1,2]
    nums = [0,0,1,1,1,2,2,3,3,4]
    ans = removeDuplicates(nums)
    print(ans, nums)
