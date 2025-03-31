#Lista przedziałów, każdy przedział to klocek [a, b].
#Klocki spadają w dół w kolejności jak w liście, a my chcemy dowiedzieć
#się, ile najmniej klocków należy usunąć, żeby powstała piramidka
inf = float('inf')
def rek(T, cache, top, i):
    if i == 0:
        return 0
    if cache[i] != -1:
        return cache[i]
    cache[i] = min(rek(T, cache, top, i-1) + 1,
                   min([rek(T, cache, top, j) + (i-j+1) for j in range(i)
                        if upper(T[i], top[j])]), i)
    if cache[i] == rek(T, cache, top, i - 1) + 1:
        top[i] = top[i-1]
    else:
        top[i] = T[i]
    return cache[i]

def upper(a, b):
    #a na wierszchu, b будемо класти
    if a[0] < b[0] or a[1] > b[1]:
        return False
    return True

def klocki(T):
    n = len(T)
    cache = [-1 for _ in range(n)]
    top = [None for _ in range(n)]
    cache[0] = 0
    top[0] = T[0]
    return rek(T, cache, top, n)

def can_be_placed(a, b):
    return a[0] <= b[0] <= a[1] and a[0] <= b[1] <= a[1]

def my_klocki(T):
    n = len(T)
    dp = [(1, 0) for _ in range(n)]
    for i in range(1, n):
        dp[i] = (dp[i][0], max(dp[i-1][0], dp[i-1][1]))
        for j in range(i):
            if can_be_placed(T[j], T[i]):
                dp[i] = (max(dp[i][0], dp[j][0] + 1), dp[i][1])
    return n - max(dp[n-1][0], dp[n-1][1])

# def my_klocki2(T):
#     n = len(T)
#     dp = [(i, i) for i in range(n)]
#     for i in range(1, n):
#         dp[i] = dp[i-1] + 1
#         for j in range(i):
#             if can_be_placed(T[j], T[i]):
#                 dp[i] = min(dp[i], dp[j] + i - j - 1)
#     print(dp)
#     return dp[n-1]

def my_klocki3(T):
    n = len(T)
    DP = [(inf, inf) for _ in range(n)]
    DP[0] = (0, 1)
    for i in range(1, n):
        DP[i] = (i, min(DP[i-1][0], DP[i-1][1]) + 1)
        for j in range(i):
            if can_be_placed(T[j], T[i]):
                DP[i] = (min(DP[i][0], DP[j][0] + i - j - 1), DP[i][1])
    return DP

T = [(0, 4), (1, 5), (1, 4), (6, 8), (2, 3), (6, 8), (6, 8)]
print(my_klocki(T))
# print(my_klocki2(T))
print(my_klocki3(T))