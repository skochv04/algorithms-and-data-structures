# Given a positive number n. Count all possible distinct binary strings (0/1)
# of length n that there are not consecutive 1's.

def count_binary_strings(n):
    dp = [0 for _ in range(n + 1)]
    dp[1] = 2
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp


n = 4
print(count_binary_strings(n))