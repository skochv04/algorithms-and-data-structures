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
        for v in G[u]:
            if not visited[v]:
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

def make_list(M):
    n = len(M)
    for i in range(n):
        for j in range(len(M[i])):
            M[i][j] += n
    for i in range(n, 2 * n):
        M.append([2 * n + 1])
    M.append([i for i in range(n)])
    M.append([])
    return M

# def make_list_2(M):
#     n = len(M)
#     G = []
#     for i in range(n):
#         G.append([2 * n + 1])
#     for i in range(n):
#         G.append(M[i])
#     G.append([i for i in range(n, 2*n)])
#     G.append([])
#     return G

def update_weights(G, path):
    for i in range(len(path)-1):
        G[path[i]].remove(path[i+1])
        G[path[i+1]].append(path[i])

def binworker( M ):
    M = make_list(M)
    n = len(M)
    count = 0
    path = find_path(M, n - 2, n - 1)
    while path:
        update_weights(M, path)
        count += 1
        path = find_path(M, n - 2, n - 1)
    return count


M = [[0, 1, 3], [2, 4], [0, 2], [3], [3, 2]]
#print(binworker(M))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
