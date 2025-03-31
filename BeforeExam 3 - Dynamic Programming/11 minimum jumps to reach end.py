# Given an array of steps that can be made forward from actual element. What is
# the minimum number of jumps it takes to go from start of an array to the end of
# an array.

inf = float('inf')

def jumps_to_end(T):
    n = len(T)
    dp = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    dp[0] = 0
    for i in range(1, n):
        for j in range(i):
            if j + T[j] >= i:
                if dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
    #printing path
    ind = n - 1
    tab = [ind]
    while parent[ind] != None:
        tab.append(parent[ind])
        ind = parent[ind]
    return tab[::-1]

T = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
print(jumps_to_end(T))