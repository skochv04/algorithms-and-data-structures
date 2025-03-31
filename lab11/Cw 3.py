#mamy tablice A wypelniona liczbami naturalnymi, mamy liczbe T i musimy sprawdzic czy z elementow tablicy A
# da sie stworzyc taki podciąg elementow z A zeby ich suma dala T

#Szukamy niekoniecznie spójny podzbior o wartości s w tablicy T
#F(s, i) = czy istniejie podciąg elementów z podzbiorów od 1 do i o sumie = s
#F(0, i) = True
#F(s, 0) = False
#F(0, 0) = True
#F(s, i) = F(s, i-1) or F(s - T[i], i-1)

def find_sum_rec(T, A):
    dp = [False for _ in range(T + 1)]
    dp[0] = True

    for num in A:
        for i in range(T, num - 1, -1):
            if dp[i - num]:
                dp[i] = True
    return dp[T]

def find_sum(a, T):
    n = len(T)
    if n == 0:
        return False
    F = [[False for b in range(a+1)] for i in range(n)]
    for i in range(n):
        F[i][0] = True
    if T[0] <= a:
        F[0][T[0]] = True
    for b in range(a + 1):
        for i in range(1, n):
            F[i][b] = F[i-1][b]
            if T[i] <= b:
                F[i][b] = F[i][b] or F[i-1][b-T[i]]
    return F

def subsetSum(a, T):
    n = len(T)
    # `T[i][j]` stores true if subset with sum `j` can be attained
    # using items up to first `i` items
    F = [[False for x in range(a + 1)] for y in range(n + 1)]
    # if the sum is zero
    for i in range(n + 1):
        F[i][0] = True
    # do for i'th item
    for i in range(1, n + 1):
        # consider all sum from 1 to sum
        for j in range(1, a + 1):
            # don't include the i'th element if `j-A[i-1]` is negative
            if T[i - 1] > j:
                F[i][j] = F[i - 1][j]
            else:
                # find the subset with sum `j` by excluding or including the i'th item
                F[i][j] = F[i - 1][j] or F[i - 1][j - T[i - 1]]
    # return maximum value
    return F[n][a]

def find_sum_test(a, T):
    n = len(T)
    dp = [[False for _ in range(a + 1)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = True
        dp[i][T[i]] = True
    for j in range(T[0] + 1, a + 1):
        dp[0][j] = dp[0][j] or dp[0][j-T[0]]
    for i in range(1, n):
        for j in range(a + 1):
            dp[i][j] = dp[i][j] or dp[i-1][j]
            if j - T[i] >= 0:
                dp[i][j] = dp[i][j] or dp[i][j-T[i]]
    return dp

def find_sum_test2(a, T):
    F = [False for _ in range(a + 1)]
    F[0] = True
    for el in T:
        F[el] = True
    for b in range(1, a + 1):
        for el in T:
            if b - el > 0:
                F[b] = F[b] or F[b - el]
    return F

def find_sum_test3(a, T):
    n = len(T)
    F = [[False for b in range(a + 1)] for i in range(n)]
    for i in range(n):
        F[i][0] = True
    for b in range(T[0], a + 1):
        F[0][b] = F[0][b - T[0]]
    for i in range(1, n):
        for b in range(a + 1):
            F[i][b] = F[i-1][b]
            if b - T[i] >= 0:
                F[i][b] = F[i][b] or F[i][b - T[i]]
    return F[-1]

def my_findsum(a, T):
    n = len(T)
    DP = [[False for _ in range(a+1)] for _ in range(n)]
    if T[0] <= a:
        DP[0][T[0]] = True
    for i in range(n):
        DP[i][0] = True
    for i in range(1, n):
        for b in range(a + 1):
            DP[i][b] = DP[i-1][b]
            if b - T[i] >= 0:
                DP[i][b] = DP[i][b] or DP[i-1][b-T[i]]
    print(*DP, sep='\n')
    return DP[-1][-1]

a = 24
T = [5, 7, 13]
print(find_sum_rec(a, T))
print(*find_sum_test(a, T), sep='\n')
print()
print(subsetSum(a, T))
print(my_findsum(a, T))