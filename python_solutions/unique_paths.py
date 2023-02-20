def uniquePaths(m: int, n: int) -> int:
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0:
                dp[0][j] = 1
            if j == 0:
                dp[i][0] = 1
            if (i != 0) and (j != 0):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m-1][n-1]


if __name__ == '__main__':
    params = [(3, 7), (3, 2), (3, 1), (1, 3)]
    for (m, n) in params:
        ans = uniquePaths(m, n)
        print(ans)
