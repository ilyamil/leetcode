def lengthOfLongestSubstring(s: str) -> int:
    left = -1
    max_len = 0
    char_to_idx = {}
    for idx, char in enumerate(s):
        if char in char_to_idx and char_to_idx[char] > left:
            left = char_to_idx[char]
        char_to_idx[char] = idx
        max_len = max(max_len, idx - left)
    return max_len


if __name__ == '__main__':
    test_cases = [
        {'input': 'aaaaa', 'output': 1},
        {'input': 'ababab', 'output': 2},
        {'input': 'abcade', 'output': 5},
        {'input': 'pwwkew', 'output': 3},
        {'input': 'abcabcbb', 'output': 3}
    ]

    for test_case in test_cases:
        ans = lengthOfLongestSubstring(test_case['input'])
        print(ans == test_case['output'], ans)
