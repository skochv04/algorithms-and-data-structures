#Zaba
inf = float('inf')
def zaba1(T):
    n = len(T)
    path = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        path[i][i] = (0, T[i], True)
    for i in range(1, n):
        path[i-1][i] = (1, T[i-1] - 1 + T[i], T[i-1] - 1 >= 0)
    for i in range(n-1):
        for j in range(i+2, n):
            path[i][j] = (1, T[i] - (j - i) + T[j], T[i] - j - i >= 0)
    for i in range(n - 1):
        for j in range(i + 2, n):
            if path[i][j-1][0] + path[j-1][j][0] < path[i][j][0] and path[i][j-1][1] + path[j-1][j][1] - T[j-1] >= 0:
                path[i][j] = (path[i][j-1][0] + path[j-1][j][0], path[i][j-1][1] + path[j-1][j][1] - T[j-1], True)
    print(*path, sep='\n')

def zaba(T):
    n = len(T)
    jumps = [0 for _ in range(n)]
    energy = [-1 for _ in range(n)]
    energy[0] = T[0]
    for i in range(1, T[0] + 1):
        jumps[i] = 1
        energy[i] = T[0] - i + T[i]
    if jumps[n-1] != 0:
        return jumps[n-1]

    for i in range(1, n):
        for j in range(i + 1, n):
            if jumps[j] == 0 or jumps[j] == jumps[i] + 1 or energy[j] == 0:
                if energy[i] - (j - i) >= 0 and energy[i] - (j - i) + T[j] > energy[j]:
                    jumps[j] = jumps[i] + 1
                    energy[j] = energy[i] - (j - i) + T[j]
    return jumps[n-1]

def my_zaba(T):
    n = len(T)
    energy = sum(T) + 1
    dp = [[(inf, 0) for _ in range(energy + 1)] for _ in range(n)]
    dp[0][T[0]] = (0, 1)
    for i in range(1, n):
        for j in range(energy):
            if dp[i-1][j+1][0] < dp[i][j][0]:
                dp[i][j] = (dp[i-1][j+1][0] + dp[i-1][j+1][1], 0)
                if dp[i][j][0] < dp[i][j + T[i]][0]:
                    dp[i][j + T[i]] = (dp[i][j][0], 1)
    print(*dp,sep='\n')
    return min(dp[-1])[0]

def my_new_zaba(T):
    n = len(T)
    B = sum(T) #максимально можлива енергія
    DP = [[(inf, 0) for _ in range(B + 1)] for _ in range(n)]
    DP[0][T[0]] = (0, 1)
    for i in range(1, n):
        for b in range(B):
            if DP[i-1][b+1][0] != inf and DP[i-1][b+1][0] + DP[i-1][b+1][1] < DP[i][b][0]:
                DP[i][b] = (DP[i-1][b+1][0] + DP[i-1][b+1][1], 0)
                if DP[i][b+T[i]][0] > DP[i][b][0]:
                    DP[i][b + T[i]] = (DP[i][b][0], 1)
    jumps = inf
    for j in range(B + 1):
        jumps = min(jumps, DP[n-1][j][0])

    print(*DP, sep='\n')
    return jumps
#T = [3, 1, 2, 0, 0, 2, 0]
#T = [3, 0, 5, 0, 0, 0, 2, 0]
T = [3, 0, 0, 5, 2, 1]
#print(zaba(T))
# print(zaba1(T))
print(my_new_zaba(T))