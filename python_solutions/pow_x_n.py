def myPow(x: float, n: int) -> float:
    # Time complexity: O(logn)
    if n == 1:
        return x
    if n == 0:
        return 1
    
    positive_power = True if n > 0 else False
    n = n if positive_power else -n

    ans = x
    cur_n = 1
    while cur_n*2 <= n:
        ans *= ans
        cur_n += cur_n

    ans = ans * myPow(x, n - cur_n)

    ans = ans if positive_power else 1/ans
    return ans


if __name__ == '__main__':
    test_cases = [
        {'x': 2., 'n': 10, 'expected':1024.},
        {'x': 2.1, 'n': 3, 'expected':9.261},
        {'x': 2., 'n': -2, 'expected':0.25},
    ]
    for test_case in test_cases:
        p = myPow(test_case['x'], test_case['n'])
        print(p, test_case['expected'])
