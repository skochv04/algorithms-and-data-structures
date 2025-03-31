# We have a map of city where are houses and shops. There are also roads (each of length 1)
# that connect a house with a house or a house with a shop. We have to find for each home
# the distance to the nearest shop.
from queue import Queue
from math import inf

def make_graph(edges):
    n = len(edges)
    max_vertex = 0
    for i in range(n):
        max_vertex = max(max_vertex, max(edges[i]))
    G = [[] for _ in range(max_vertex + 1)]
    for i in range(n):
        G[edges[i][0]].append(edges[i][1])
        G[edges[i][1]].append(edges[i][0])
    return G

def BFS(G, shops, s = 0):
    n = len(G)
    queue = Queue()
    visited = [False for _ in range(n)]
    d = [inf for _ in range(n)]
    visited[s] = True
    queue.put(s)
    while not queue.empty():
        u = queue.get()
        flag = False
        if u in shops:
            d[u] = 0
            flag = True
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                queue.put(v)
            if v in shops and u not in shops:
                d[u] = 1
                flag = True
        if not flag:
            min_dist = inf
            for i in G[u]:
                min_dist = min(min_dist, d[i])
                d[u] = min_dist + 1
    return d

def houses_and_shops(roads, shops):
    G = make_graph(roads)
    return BFS(G, shops)

roads = [[0, 1], [0, 2], [0, 3], [1, 3], [1, 4], [1, 5], [2, 5], [2, 6], [2, 7], [3, 6], [3, 8],
         [4, 8], [4, 5], [5, 7], [6, 7], [8, 9], [9, 10], [9, 11], [10, 13], [11, 12], [12, 13]]
shops = [2, 3, 9]
print(houses_and_shops(roads, shops))