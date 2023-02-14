def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    prev = 2
    prev_prev = 1
    ans = 0
    for _ in range(n - 2):
        ans = prev + prev_prev
        prev_prev = prev
        prev = ans
    return ans