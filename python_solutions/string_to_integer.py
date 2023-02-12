INT32_MIN = -2**31
INT32_MAX = 2**31 - 1
DIGITS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}


def myAtoi(s: str) -> int:
    N = len(s)
    integer = 0
    positive = True
    seen_sign = False
    seen_digits = False
    for i in range(N):
        if s[i] == ' ':
            if (not seen_digits) and (not seen_sign):
                continue
            else:
                break
        elif s[i] == '0' and not seen_digits:
            seen_digits = True
        elif s[i] in ['-', '+']:
            if seen_sign or seen_digits:
                break
            seen_sign = True
            if s[i] == '-':
                positive = False
        elif (s[i] not in DIGITS):
            break
        else:
            seen_digits = True
            if integer == INT32_MAX // 10:
                if positive and (s[i] in ['8', '9']):
                    return INT32_MAX
                if not positive and (s[i] in ['8', '9']):
                    return INT32_MIN
            elif integer > INT32_MAX // 10:
                return INT32_MAX if positive else INT32_MIN
            integer = integer * 10 + int(s[i])

    return integer if positive else -integer


if __name__ == '__main__':
    test_cases = [
        {'input': '42', 'output': 42},
        {'input': '   -42', 'output': -42},
        {'input': '4193 with words', 'output': 4193},
        {'input': '+-12', 'output': 0},
        {'input': 'words and 987', 'output': 0},
        {'input': '00000-42a1234', 'output': 0},
        {'input': '21474836460', 'output': 2147483647},
        {'input': '2147483646', 'output': 2147483646},
        {'input': '010', 'output': 10},
        {'input': '   +0 123', 'output': 0},
        {'input': '-91283472332', 'output': INT32_MIN},
        {'input': '  +  413', 'output': 0}
    ]

    for test_case in test_cases:
        ans = myAtoi(test_case['input'])
        print(ans == test_case['output'], ans)
