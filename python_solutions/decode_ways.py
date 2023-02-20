from string import ascii_lowercase


def numDecodings(s: str) -> int:
    nums = {i for i in range(1, 27)}
    if not s:
        return 0

    N = len(s)
    dp = [0 for _ in range(N + 1)]
    dp[0] = 1
    dp[1] = 0 if s[0] == '0' else 1
    for i in range(1, N):
        if int(s[i]) in nums:
            dp[i+1] += dp[i]
        if int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) in nums:
            dp[i+1] += dp[i-1]
    return dp[N]


if __name__ == '__main__':
    test_cases = [
        {'input': "12", 'output': 2},
        {'input': "226", 'output': 3},
        {'input': "06", 'output': 0},
        {'input': '1223', 'output': 5},
        {'input': "2101", 'output': 1},
        {'input': "10", 'output': 1}
    ]
    for i, tc in enumerate(test_cases):
        ans = numDecodings(tc['input'])
        print(i, ans)