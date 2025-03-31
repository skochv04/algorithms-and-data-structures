from zad6testy import runtests
from collections import deque

def find_path(G, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    d = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = deque()
    d[s] = 0
    visited[s] = True
    Q.append(s)
    while len(Q):
        u = Q.popleft()
        for v in range(n):
            if G[u][v] and not visited[v]:
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
                Q.append(v)
    tab = None
    if parent[t] != None:
        ind = t
        tab = []
        while ind != s:
            tab.append(ind)
            ind = parent[ind]
        tab.append(ind)
        tab = tab[::-1]
    return tab

def make_matrix(M):
    n = len(M)
    G = [[0 for _ in range(2*n+2)] for _ in range(2*n+2)]
    for i in range(n):
        for j in M[i]:
            G[i][j+n] = 1
    for j in range(n):
        G[2*n][j] = 1
    for i in range(n, 2*n):
        G[i][2*n+1] = 1
    return G

def min_weight(G, path):
    w = G[path[0]][path[1]]
    for i in range(1, len(path) - 1):
        if G[path[i]][path[i+1]] < w:
            w = G[path[i]][path[i + 1]]
    return w

def update_weights(G, path, w):
    # if len(path) == 1:
    #     G[path[0]].remove(path[0])
    for i in range(len(path)-1):
        G[path[i]][path[i+1]] -= w
        G[path[i+1]][path[i]] += w
        # G[path[i]].remove(path[i+1])
        # G[path[i+1]].append(path[i])

def binworker( M ):
    # M = make_matrix(M)
    n = len(M)
    # M = [[0 for _ in range(n)] for _ in range(n)]
    s = n - 2
    t = n - 1
    count = 0
    path = find_path(M, s, t)
    while path:
        # w = min_weight(M, path)
        update_weights(M, path, 1)
        count += 1
        path = find_path(M, s, t)
    return count


M = [[0, 1, 3], [2, 4], [0, 2], [3], [3, 2]]
print(binworker(M))
# for i in range(len(G)):
#     for j in range(len(G)):
#         print(G[i][j], end=" ")
#     print()

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
