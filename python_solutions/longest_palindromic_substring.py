from typing import Tuple


def expand_around_center(s: str, start_left: int, start_right: int)\
    -> Tuple[int, int]:
    cur_left = start_left
    cur_right = start_right
    left = cur_left
    right = cur_right
    while (cur_left >= 0) and (cur_right < len(s)):
        if s[cur_left] == s[cur_right]:
            left = cur_left
            right = cur_right
        else:
            break
        cur_left -= 1
        cur_right += 1
    return left, right


def longestPalindrome(s: str) -> str:
    lp = ''
    for i in range(len(s)):
        left, right = expand_around_center(s, i, i)
        if (right - left + 1) > len(lp):
            lp = s[left: right + 1]
        if (i != len(s) - 1) and (s[i] == s[i + 1]):
            left, right = expand_around_center(s, i, i + 1)
            if (right - left + 1) > len(lp):
                lp = s[left: right + 1]
    return lp


if __name__ == '__main__':
    test_cases = [
        {'input': 'babad', 'output': 'bab'},
        {'input': 'bacbbad', 'output': 'bb'},
        {'input': 'cbbd', 'output': 'bb'},
    ]

    for test_case in test_cases:
        ans = longestPalindrome(test_case['input'])
        print(ans == test_case['output'], ans)