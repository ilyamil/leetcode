def isValid(s: str) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(n)
    stack = []
    for char in s:
        if stack:
            if (char == ')' and stack[-1] == '(')\
                or (char == ']' and stack[-1] == '[')\
                or ((char == '}' and stack[-1] == '{')):
                _ = stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)
    return True if not stack else False


if __name__ == '__main__':
    test_cases = [
        {'input': "()", 'output': True},
        {'input': "()[]{}", 'output': True},
        {'input': "(]", 'output': False},
        {'input': "({[)", 'output': False}
    ]

    for test_case in test_cases:
        ans = isValid(test_case['input'])
        print(ans == test_case['output'])