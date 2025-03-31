# There is a civil war going on in one country. As part of the sabotage, the rebels want to prevent
# telegraphic communication from A to B. We are given a list of cities and telegraph lines between them.
# Telegraphic lines are directed. Each line has a cost associated with destroying it. We want to select
# a set of connections to be destroyed with a total minimum cost. We are not only interested in the cost,
# but also which specific telegraph lines are to be destroyed.

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
            if G[u][v] > 0 and not visited[v]:
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
        w = min_weight(G, my_path)
        count += w
        update_weights(G, my_path, w)
        my_path = find_path(G, s, t)
    return count

def DFS_visit(G, s, visited):
    n = len(G)
    visited[s] = True
    for i in range(n):
        if G[s][i] > 0 and not visited[i]:
            DFS_visit(G, i, visited)

def sabotage(G, A, B):
    flow = ford_fulkerson(G, A, B)
    n = len(G)
    visited = [False for _ in range(n)]
    DFS_visit(G, 0, visited)

    mini = 0
    edges = []
    for i in range(n):
        local_mini = 0
        for j in range(n):
            if visited[i] and not visited[j] and G[i][j] == 0 and G[j][i] > 0:
                edges.append((i, j))
                local_mini += 1
        # if local_mini != 0:
        mini += local_mini
    return flow, (mini, edges)

G =     [[-1, 8, 5, -1, -1, -1, -1, -1],
         [-1, -1, -1, 4, 2, -1, -1, -1],
         [-1, -1, -1, -1, -1, 4, -1, -1],
         [-1, -1, -1, -1, -1, -1, 2, -1],
         [-1, -1, -1, 3, -1, 2, -1, -1],
         [-1, -1, -1, -1, -1, -1, 4, 6],
         [-1, -1, -1, -1, -1, -1, -1, 4],
         [-1, -1, -1, -1, -1, -1, -1, -1]]
A, B = 0, 7
print(sabotage(G, A, B))