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
        while ind != parent[s]:
            tab.append(ind)
            ind = parent[ind]
        tab = tab[::-1]
    return tab

def min_weight(G, path):
    w = G[path[0]][path[1]]
    for i in range(1, len(path) - 1):
        if G[path[i]][path[i+1]] < w:
            w = G[path[i]][path[i + 1]]
    return w

def update_weights(G, path, w):
    for i in range(len(path)-1):
        G[path[i]][path[i+1]] -= w
        G[path[i+1]][path[i]] += w

def binworker( M ):
    n = len(M)
    station = [False for _ in range(n)]
    count = 0
    for u in range(n):
        for v in M[u]:
            if not station[v]:
                station[v] = True
                count += 1
                # path = find_path(M, u, v)
                # w = min_weight(M, path)
    return count

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
