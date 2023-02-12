from typing import List

DIGIT_LETTERS_MAPPING = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

def letterCombinations(digits: str) -> List[str]:
    combination = []
    last_combination = []
    for digit in digits:
        letters = DIGIT_LETTERS_MAPPING[digit]
        if not last_combination:
            combination.extend(letters)
            last_combination = letters
            continue
        combination = []
        for el in last_combination:
            for letter in letters:
                combination.append(el + letter)
        last_combination = combination
    return combination


if __name__ == '__main__':
    test_cases = [
        {'input': '23', 'output': ["ad","ae","af","bd","be","bf","cd","ce","cf"]},
        {'input': '', 'output': []},
        {'input': '2', 'output': ["a","b","c"]},
    ]

    for test_case in test_cases:
        ans = letterCombinations(test_case['input'])
        print(ans == test_case['output'], ans)