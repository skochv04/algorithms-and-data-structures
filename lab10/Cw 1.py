#Podstawowy algorytm Forda-Fulkersona
#Graf skierowany, ale na nieskierowanym też zadziała
# G = deepcopy(M)
# from copy import deepcopy
from collections import deque

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

def min_weight(G, path):
    #Проходимо по всьому шляху і шукаємо мінімальну вагу на ньому
    w = G[path[0]][path[1]]
    for i in range(1, len(path) - 1):
        w = min(w, G[path[i]][path[i + 1]])
    return w

def update_weights(G, path, w):
    for i in range(len(path)-1):
        G[path[i]][path[i+1]] -= w
        G[path[i+1]][path[i]] += w

def ford_fulkerson(G, s, t):
    n = len(G)
    count = 0
    my_path = find_path(G, s, t)
    while my_path:
        #mamy ścieżke, musimy zaktualizować
        w = min_weight(G, my_path)
        count += w
        update_weights(G, my_path, w)
        my_path = find_path(G, s, t)
    return count

G = [[0, 10, 0, 10, 0, 0],
     [0, 0, 4, 2, 8, 0],
     [0, 0, 0, 0, 0, 10],
     [0, 0, 0, 0, 9, 0],
     [0, 0, 6, 0, 0, 10],
     [0, 0, 0, 0, 0, 0]]

print(ford_fulkerson(G, 0, 5))
