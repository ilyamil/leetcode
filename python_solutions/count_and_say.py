def countAndSay(n: int) -> str:
    ans = '1'
    if n == 1:
        return ans

    new_ans = ''
    for _ in range(n - 1):
        digit = ans[0]
        num = 1
        for idx in range(1, len(ans)):
            if ans[idx] == digit:
                num += 1
            else:
                new_ans += str(num) + digit
                digit = ans[idx]
                num = 1
        new_ans += str(num) + digit
        ans = new_ans
        new_ans = ''
    return ans


if __name__ == '__main__':
    test_cases = [
        {'input': 1, 'output': '1'},
        {'input': 2, 'output': '11'},
        {'input': 3, 'output': '21'},
        {'input': 4, 'output': '1211'},
        {'input': 5, 'output': '111221'}
    ]
    for test_case in test_cases:
        ans = countAndSay(test_case['input'])
        print(ans == test_case['output'])
