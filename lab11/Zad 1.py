#Шахматна дошка 8*8, король стоїть на лівому нижньому полі, може переміщатися тільки вправо, вгору і по діагоналі.
#Шукаємо мінімальний кошт проходу з лівого нижнього в праве верхнє поле.

inf = float('inf')

def path(A):
    n = len(A)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[n-1][0] = 0
    for i in range(n-2, -1, -1):
        dp[i][0] = dp[i+1][0] + A[i][0]
    for i in range(1, n):
        dp[n-1][i] = dp[n-1][i-1] + A[n-1][i]
    for i in range(n-2, -1, -1):
        for j in range(1, n):
            dp[i][j] = min(dp[i+1][j-1], dp[i][j-1], dp[i+1][j]) + A[i][j]
    return dp[0][n-1]

# def king(A):
#     n = len(A)
#     dp = [[inf for _ in range(n)] for _ in range(n)]
#     dp[0][n-1] = A[0][n-1]
#     for j in range(n - 2, -1, -1):
#         dp[0][j] = dp[0][j+1] + A[0][j]
#     for i in range(1, n):
#         dp[i][n-1] = dp[i-1][n-1] + A[i][n-1]
#     for i in range(1, n):
#         for j in range(n-2, -1, -1):
#             dp[i][j] = min(dp[i-1][j], dp[i][j+1], dp[i-1][j+1]) + A[i][j]
#
#     return dp

def dynamik_path(T):
    n = len(T)
    DP = [[inf for _ in range(n)] for _ in range(n)]
    DP[n-1][0] = 0
    for i in range(n - 2, -1, -1):
        DP[i][0] = DP[i+1][0] + T[i][0]
        DP[n-1][n-1-i] = DP[n-1][n-2-i] + T[n-1][n-1-i]
    for i in range(n - 2, -1, -1):
        for j in range(1, n):
            DP[i][j] = min(DP[i+1][j], DP[i][j-1], DP[i+1][j-1]) + T[i][j]
    print(*DP, sep='\n')

T = [[9, 9, 9, 9, 9, 9, 1, 9],
     [9, 9, 9, 9, 9, 1, 9, 2],
     [9, 9, 9, 9, 9, 9, 1, 9],
     [9, 9, 9, 9, 9, 9, 9, 9],
     [9, 9, 9, 9, 9, 9, 9, 9],
     [9, 9, 9, 9, 9, 9, 9, 9],
     [9, 9, 9, 9, 9, 9, 9, 9],
     [0, 9, 9, 9, 9, 9, 9, 9]]

n = len(T)

#print(path(T))
#print(*king(T),sep='\n')
print(dynamik_path(T))