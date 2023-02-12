from typing import List


def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0
    while left != right:
        cur_area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, cur_area)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_area


if __name__ == '__main__':
    test_cases = [
        {'input': [1,8,6,2,5,4,8,3,7], 'output': 49},
        {'input': [1, 1], 'output': 1},
    ]

    for test_case in test_cases:
        ans = maxArea(test_case['input'])
        print(ans == test_case['output'], ans)