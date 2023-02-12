INT_MIN = -2**31
INT_MAX = 2**31 - 1


def reverse(x: int) -> int:
    if (x == INT_MAX) or (x == INT_MIN):
        return 0

    is_positive = True if x >= 0 else False
    if not is_positive:
        x = abs(x)

    rx = 0
    while x != 0:
        if rx > INT_MAX // 10:
            return 0
        rx = rx * 10 + x % 10
        x //= 10

    return rx if is_positive else -rx


if __name__ == '__main__':
    test_cases = [
        {'input': 123, 'output': 321},
        {'input': -123, 'output': -321},
        {'input': 120, 'output': 21},
        {'input': 1_000_000_000, 'output': 1},
        {'input': 1_000_000_009, 'output': 0},
    ]

    for test_case in test_cases:
        ans = reverse(test_case['input'])
        print(ans == test_case['output'], ans)