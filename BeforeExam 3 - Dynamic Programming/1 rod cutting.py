# Given a rod of length n inches and a table of prices T[i] for i = [1, 2, ..., n].
# Determine the maximum dp r[n] obtainable by cutting up the rod and selling
# the pieces.

def rod_cutting_rec(T, n):
    dp = [-1 for _ in range(n+1)]
    return rod_cutting(T, dp, n)

def rod_cutting(T, dp, n):
    if dp[n-1] <= 0:
        if n == 0:
            dp[n-1] = 0
        else:
            for i in range(n):
                dp[n-1] = max(dp[n-1], T[i]+rod_cutting(T, dp, n-i-1))
    return dp[n-1]

def rod_cutting_bottom_up(T, n):
    dp = [-1 for _ in range(n+1)]
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] = max(dp[i], dp[i - j - 1] + T[j])
    return dp[n]

def rod_cutting_bottom_up_extended(T, n):
    dp = [-1 for _ in range(n+1)]
    size = [0 for _ in range(n+1)]
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            if dp[i] < dp[i - j - 1] + T[j]:
                dp[i] = dp[i - j - 1] + T[j]
                size[i] = j + 1
    return dp, size

def print_rod_cutting(T, n):
    dp, size = rod_cutting_bottom_up_extended(T, n)
    print(dp, size)
    tab = []
    while n > 0:
        tab.append(size[n])
        n -= size[n]
    print(tab)

T = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 34, 34, 30, 49, 45]
n = 15
print_rod_cutting(T, n)