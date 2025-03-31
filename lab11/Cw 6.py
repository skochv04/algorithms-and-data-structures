# ciag od A_0 do A_(n-1)
# chcemy go podzielic na dokladnie k podciagow spojnych
# oraz zeby najwieksza suma elementow w kazdym podciagu spojnym byla mozliwie najmniejsza

# np:
# 0, 3, 7, 8, 12, 3, 4, -5
# fragmenty: (0, 3, 7, 8), (12, 3), (4, -5)
#             suma 18       suma 15  suma -1, a wiec koszt to 18 (najwieksza z sum)
# fragmenty: (0, 3, 7), (8, 12, 3), (4, -5)
#             suma 10    suma 23     suma -1, a wiec koszt to 23


# A - ciag wejsciowy
# f(i, j, m) - najwieksza suma fragmentu w optymalnym (zgodnym z warunkami zadania) podziale
#               ciagu A od indeksu i do indeksu j na m fragmentow


# PD - zakodowac zad 4 w n logn

def optimal_division(A, k):
    n = len(A)
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for x in range(j-1, i):
                dp[i][j] = min(dp[i][j], max(dp[x][j - 1], prefix_sum[i] - prefix_sum[x]))
    print(*dp, sep='\n')

    return dp[n][k]


# Приклад використання
A = [0, 3, 7, 8, 12, 3, 4, -5]
T = [5, 10, 30, 20, 15]
# A = [1, 4, 5]
k = 3
result = optimal_division(T, k)
print(result)