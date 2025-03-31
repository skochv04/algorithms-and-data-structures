#2D problem plecakowy
#Opróć ceny i wagi przedmiotu, mamy jeszcze jego wysokość, oraz liczbę-limit H.

def knapsack(W, P, H, B, C):
    n = len(W)
    F = [[[0 for _ in range(C + 1)] for _ in range(B + 1)] for _ in range(n)]
    parent = [[[[] for _ in range(C + 1)] for _ in range(B + 1)] for _ in range(n)]
    for c in range(H[0], C + 1):
        for b in range(W[0], B + 1):
            F[0][b][c] = P[0]
            parent[0][b][c] = [0]
    for c in range(C + 1):
        for b in range(B + 1):
            for i in range(1, n):
                F[i][b][c] = F[i - 1][b][c]
                parent[i][b][c] = parent[i - 1][b][c]
                if b - W[i] >= 0 and c - H[i] >= 0:
                    if F[i][b][c] < F[i-1][b-W[i]][c-H[i]] + P[i]:
                        F[i][b][c] = F[i-1][b-W[i]][c-H[i]] + P[i]
                        parent[i][b][c] = parent[i - 1][b - W[i]][c - H[i]] + [i]
    return F[n - 1][B][C], parent[n - 1][B][C]

P = [10, 20, 5, 15, 3, 8]
W = [0, 7, 27, 4, 1, 5] # <= B
H = [4, 6, 2, 5, 7, 1] # <= C
B = 10
C = 14

print(knapsack(W, P, H, B, C))