def knapsack(W, P, B):
    n = len(W)
    F = [[0 for b in range(B+1)] for i in range(n)]
    parent = [[[] for b in range(B + 1)] for i in range(n)]
    for b in range(W[0], B+1):
        F[0][b] = P[0]
        parent[0][b] = [0]
    for b in range(B+1):
        for i in range(1, n):
            F[i][b] = F[i-1][b]
            parent[i][b] = parent[i-1][b]
            if b - W[i] >= 0:
                if F[i][b] < F[i-1][b-W[i]] + P[i]:
                    F[i][b] = F[i-1][b-W[i]] + P[i]
                    parent[i][b] = parent[i-1][b-W[i]] + [i]
    # print(*F, sep='\n')
    # print()
    # print(*parent, sep='\n')
    return F[n-1][B], parent[n-1][B]

W = [3, 7, 27, 4, 1, 5]
P = [10, 20, 5, 15, 3, 8]
B = 10
print(knapsack(W, P, B))