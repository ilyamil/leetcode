SYMBOL_MAPPING = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
}


def romanToInt(s: str) -> int:
    N = len(s)
    integer = 0
    i = 0
    while i < N:
        if i != (N - 1) and s[i: i + 2] in SYMBOL_MAPPING.keys():
            integer += SYMBOL_MAPPING[s[i: i + 2]]
            i += 2
        else:
            integer += SYMBOL_MAPPING[s[i]]
            i += 1
    return integer


if __name__ == '__main__':
    test_cases = [
        {'input': "III", 'output': 3},
        {'input': "LVIII", 'output': 58},
        {'input': "MCMXCIV", 'output': 1994}
    ]

    for test_case in test_cases:
        ans = romanToInt(test_case['input'])
        print(ans == test_case['output'], ans)