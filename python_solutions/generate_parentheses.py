from typing import List


def backtrack(parentheses, n, cur, num_open, num_close):
    if len(cur) == 2*n:
        parentheses.append(cur)
        return

    if num_open < n:
        backtrack(parentheses, n, cur + '(', num_open + 1, num_close)
    if num_open > num_close:
        backtrack(parentheses, n, cur + ')', num_open, num_close + 1)


def generateParenthesis(n: int) -> List[str]:
    parentheses = []
    backtrack(parentheses, n, '', 0, 0)
    return parentheses


if __name__ == '__main__':
    test_cases = [
        {'input': 1, 'output': ['()']},
        {'input': 2, 'output': ['()()', '(()))']},
        {'input': 3, 'output': ["((()))","(()())","(())()","()(())","()()()"]}
    ]
    for test_case in test_cases:
        ans = generateParenthesis(test_case['input'])
        print(ans)