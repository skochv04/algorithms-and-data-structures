# A country has n cities. Initially, there is no road in the country. One day, the king decides to
# construct some roads connecting pairs of cities. Roads can be traversed either way. He wants those
# roads to be constructed in such a way that it is possible to go from each city to any other city
# by traversing at most two roads. You are also given m pairs of cities — roads cannot be constructed
# between these pairs of cities. Our task is to construct the minimum number of roads that still satisfy
# the above conditions. The constraints will guarantee that this is always possible.
from queue import Queue

def BFS(G):
    visited = [False for _ in range(n)]
    d = [-1 for _ in range(n)]
    q = Queue()
    d[0] = 0
    visited[0] = True
    q.put(0)
    while not q.empty():
        u = q.get()
        for v in range(n):
            if G[u][v] and not visited[v]:
                d[v] = d[u] + 1
                visited[v] = True
                q.put(v)
    return visited

def road_construction(n, m, T):
    G = [[0 for _ in range(n)] for _ in range(n)]
    for u, v in T:
        G[u][v] = -1
        G[v][u] = -1
    for i in range(1, n):
        if G[0][i] != -1 and G[i][0] != -1:
            G[0][i] = 1
            G[i][0] = 1

    ind = 0
    for i in range(1, n):
        if G[ind][i] == -1:
            while G[ind][i] == -1 and ind < n - 1:
                ind += 1
            while G[ind][0] != 1 and ind < n - 1:
                ind += 1
            if ind == i:
                while G[ind][i] == -1 and ind < n - 1:
                    ind += 1
                while G[ind][0] != 1 and ind < n - 1:
                    ind += 1
            if ind < n-1 and ind != i:
                G[ind][i] = 1
                G[i][ind] = 1
            ind = 0

    for i in range(n): #прибираємо зайве
        for j in range(n):
            if G[i][j] == -1:
                G[i][j] = 0

    visited = BFS(G)
    for i in range(n):
        if not visited[i]:
            return None
    return G


n = 4
m = 1
T = [(0, 3), (3, 1)]
print(road_construction(n, m, T))