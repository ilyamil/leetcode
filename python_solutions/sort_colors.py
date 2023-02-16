from typing import List


def sortColors(nums: List[int]) -> None:
    red, white, blue = 0, 0, len(nums) - 1
    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1


if __name__ == '__main__':
    test_cases = [
        {'input': [0], 'output': [0]},
        {'input': [0, 0], 'output': [0, 0]},
        {'input': [2, 0], 'output': [0, 2]},
        {'input': [1,0,1], 'output': [0, 1, 1]},
        {'input': [0, 1, 2], 'output': [0, 1, 2]},
        {'input': [2,0,2,1,1,0], 'output': [0,0,1,1,2,2]},
        {'input': [2,0,1], 'output': [0,1,2]}
    ]
    for test_case in test_cases:
        nums = test_case['input']
        sortColors(nums)
        #print(nums)
        assert nums == test_case['output']
