def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    if x < 4:
        return 1

    output = 2
    while True:
        output += 1
        sq = output * output
        if sq == x:
            break
        elif sq > x:
            output -= 1
            break
    return output


if __name__ == '__main__':
    test_cases = [
        {'input': 4, 'output': 2},
        {'input': 8, 'output': 2},
        {'input': 9, 'output': 3},
    ]
    for test_case in test_cases:
        ans = mySqrt(test_case['input'])
        print(ans, ans == test_case['output'])