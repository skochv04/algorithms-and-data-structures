# We are given a distance n. Count the total number of ways to cover the distance
# using 1, 2, 3 steps.

def staircase_jump(n):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 2
    for i in range(3, n + 1):
        dp[i] += dp[i-1] + dp[i-2] + dp[i-3]
    return dp


n = 6
print(staircase_jump(n))