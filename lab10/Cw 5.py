# Mamy gotowy algorytm forda-fulkersona, mamy wiele źródeł i wiele ujść -> dodajemy wspólne źródło i wspólne ujście ->
# implementacja redukcji, dana lista tupli

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
            if not visited[v] and G[u][v]:
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
                Q.append(v)
    tab = None
    w = float('inf')
    if parent[t] != None:
        ind = t
        tab = []
        w = float('inf')
        while ind != parent[s]:
            if parent[ind] != None:
                for i in range(n):
                    if i == ind:
                        w = min(w, G[parent[ind]][i])
            tab.append(ind)
            ind = parent[ind]
        tab = tab[::-1]
    return tab, w

def update_weights(G, path, w):
    for i in range(len(path)-1):
        G[path[i]][path[i+1]] -= w
        G[path[i+1]][path[i]] += w

def suma(G, el, type):
    n = len(G)
    suma = 0
    if type:
        for i in range(n):
            suma += G[el][i]
    else:
        for i in range(n):
            suma += G[i][el]
    return suma

def change(G, s, t):
    n = len(G)
    for i in range(n):
        G[i].append(0)
        G[i].append(0)
    G.append([0 for _ in range(n+2)])
    G.append([0 for _ in range(n+2)])
    for el in s:
        G[n][el] = suma(G, el, True)
    for el in t:
        G[el][n + 1] = suma(G, el, False)
    return G

def ford_fulkerson(G, s, t):
    G = change(G, s, t)
    n = len(G)
    count = 0
    my_path, w = find_path(G, n-2, n-1)
    while my_path:
        #mamy ścieżke, musimy zaktualizować
        count += w
        update_weights(G, my_path, w)
        my_path, w = find_path(G, n-2, n-1)
    return count

G = [[0,  0,  0, 14,  0,  0,  0,  0,  0,  0,  0],
     [0,  0,  0,  4, 16,  0,  0,  0,  0,  0,  0],
     [0,  0,  0,  0, 0,  10,  0,  0,  0,  0,  0],
     [0,  0,  0,  0,  6,  0,  0,  0,  0,  0,  0],
     [0,  0,  0,  0,  0,  1,  0,  5,  0,  0,  0],
     [0,  0,  0,  0,  0,  0,  3,  0,  0,  0,  8],
     [0,  0,  0,  0,  0,  0,  0,  0,  12, 0,  0],
     [0,  0,  0,  0,  0,  0,  9,  0,  7,  0,  0],
     [0,  0,  0,  0,  0,  0,  0,  0,  0,  17, 0],
     [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
     [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]

s = [0, 1, 2]
t = [9, 10]

print(ford_fulkerson(G, s, t))
