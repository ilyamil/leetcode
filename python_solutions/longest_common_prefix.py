from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    strs = sorted(strs)
    if strs[0] == '':
        return ''
    max_i = -1
    stop = False
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if (i < len(strs[j])) and (strs[j][i] == strs[0][i]):
                continue
            else:
                stop = True
                break
        if stop:
            break
        max_i = i
    return strs[0][:max_i + 1] if max_i >= 0 else ''


if __name__ == '__main__':
    test_cases = [
        {'input': ["flower","flow","flight"], 'output': 'fl'},
        {'input': ["dog","racecar","car"], 'output': ''},
        {'input': ["rain","race", ''], 'output': ''},
    ]

    for test_case in test_cases:
        ans = longestCommonPrefix(test_case['input'])
        print(ans == test_case['output'], ans)