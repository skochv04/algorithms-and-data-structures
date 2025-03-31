from zad6testy import runtests
from collections import deque

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

def construct(M):
    n = len(M)
    G = [[0 for _ in range(2*n + 2)] for _ in range(2*n + 2)]
    for i in range(n):
        G[i][2*n+1] = 1
        G[2*n][i+n] = 1
        for j in M[i]:
            G[i + n][j] = 1
    return G

def find_path(G, s, t):
    #BFS/DFS
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
        while ind != parent[s]:
            tab.append(ind)
            ind = parent[ind]
        tab = tab[::-1]
    return tab

def ford_fulkerson(G, s, t):
    n = len(G)
    count = 0
    my_path = find_path(G, s, t)
    while my_path:
        count += 1
        for i in range(len(my_path) - 1):
            G[my_path[i]][my_path[i + 1]] -= 1
            G[my_path[i + 1]][my_path[i]] += 1
        my_path = find_path(G, s, t)
    return count

def binworker( M ):
    G = construct(M)
    n = len(G)
    return ford_fulkerson(G, n-2, n-1)

M = [ [ 0, 1, 3], # 0
    [ 2, 4], # 1
    [ 0, 2], # 2
    [ 3 ], # 3
    [ 3, 2] ]
print(binworker(M))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )