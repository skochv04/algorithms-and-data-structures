#Аналогічно, але з верхнього лівого в нижнє праве

inf = float('inf')

def path(A, w, k):
    n = len(T)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = 0
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + A[i][0]
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + A[0][i]
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + A[i][j]
    return dp


T = [[9, 9, 9, 9, 9, 9, 1, 9],
     [9, 9, 9, 9, 9, 1, 9, 2],
     [9, 9, 9, 9, 9, 9, 1, 9],
     [9, 9, 9, 9, 9, 9, 9, 9],
     [9, 9, 9, 9, 9, 9, 9, 9],
     [9, 9, 9, 9, 9, 9, 9, 9],
     [9, 9, 9, 9, 9, 9, 9, 9],
     [0, 9, 9, 9, 9, 9, 9, 9]]

n = len(T)
print(*path(T, n-1, 0),sep='\n')