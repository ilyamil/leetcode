INT_MIN = -2147483648
INT_MAX = 2147483647


def divide(dividend: int, divisor: int) -> int:
    if dividend == 0:
        return 0
    if divisor == -1:
        if dividend == INT_MIN:
            return INT_MAX
        else:
            return -dividend
    if divisor == 1:
        return dividend

    positive = True
    if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
        positive = False
    dividend = dividend if dividend > 0 else -dividend
    divisor = divisor if divisor > 0 else -divisor

    # Slow Solution: O(n), n = value of divisor
    # ans = 0
    # while dividend >= divisor:
    #     dividend -= divisor
    #     ans += 1

    # Fast Solution: O(logn), n = value of divisor
    quotient = 0
    cur_sum = divisor
    while cur_sum <= dividend:
        current_quotient = 1
        while (cur_sum + cur_sum) <= dividend:
            cur_sum += cur_sum
            current_quotient += current_quotient
        dividend -= cur_sum
        cur_sum = divisor
        quotient += current_quotient
    return quotient if positive else -quotient


if __name__ == '__main__':
    test_cases = [
        (10, 3, 3), (7,-3,-2), (0, 1, 0), (INT_MIN, 1, INT_MIN), (INT_MIN, -1, INT_MAX)
    ]
    for (a, b, ans) in test_cases:
        res = divide(a, b)
        print(res, ans)
