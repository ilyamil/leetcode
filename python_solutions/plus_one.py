from typing import List

def plusOne(digits: List[int]) -> List[int]:
    N = len(digits) - 1
    rem = 1
    for i in range(N, -1, -1):
        if digits[i] + rem == 10:
            digits[i] = 0
            rem = 1
        else:
            digits[i] += 1
            rem = 0
            break
    
    if rem:
        digits.insert(0, 1)
    return digits


if __name__ == '__main__':
    test_cases = [
        {'input': [1, 2, 3], 'output': [1, 2, 4]},
        {'input': [1, 2, 9], 'output': [1, 3, 0]},
        {'input': [9, 9, 9], 'output': [1, 0, 0, 0]},
    ]
    for test_case in test_cases:
        ans = plusOne(test_case['input'])
        print(ans, ans == test_case['output'])
