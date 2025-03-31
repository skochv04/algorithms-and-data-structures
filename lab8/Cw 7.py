#Stacja benzynowa
#A     B
#krawędzie mają dł w kilometrach. W każdym wierzchołku jest stacja z c[i] - cena za litr paliwa
#D - pojemność baku w aucie
# Dojechać jak najtaniej

from queue import PriorityQueue

def relax(u, v, l, d, parent, queue):
    if d[v] > d[u] + l:
        d[v] = d[u] + l
        parent[v] = u
        queue.put((d[v], v))

def cheap(G, a, b, D, c):
    n = len(G)
    for i in range(n):
        G[i] = Dijkstra(G, i)
    d = [float('inf') for _ in range(n)]
    # L = D
    parent = [None for _ in range(n)]
    Q = PriorityQueue()
    d[a] = 0
    Q.put((d[a], a))
    while not Q.empty():
        du, u = Q.get()
        if d[u] == du:
            for v in range(n):
                l = G[u][v]
                if l != 0 and D - l > 0:
                    l *= c[u]
                    relax(u, v, l, d, parent, Q)
    B = b
    path = [b]
    while b != a:
        if parent[b] == None:
            return None
        b = parent[b]
        path.append(b)
    for i in range(len(path)-1, -1, -1):
        print(path[i], end=" ")
    print()
    return d[B]

def Dijkstra(G, s):
    n = len(G)
    parent = [None for _ in range(n)]
    d = [float('inf') for _ in range(n)]
    q = PriorityQueue()
    d[s] = 0
    q.put((d[s], s))
    while not q.empty():
        du, u = q.get()
        if d[u] == du:
            for v in range(n):
                l = G[u][v]
                if l != 0:
                    relax(u, v, l, d, parent, q)
    return d

# G = [[(1, 28), (2, 67), (5, 44)],
#      [(0, 28), (2, 45)],
#      [(0, 67), (1, 45), (3, 16), (4, 29)],
#      [(2, 16), (4, 30), (5, 50)],
#      [(2, 29), (3, 30), (5, 11)],
#      [(0, 44), (3, 50), (4, 11)]]

# G = [[0, 28, 67, 0, 0, 44],
#      [28, 0, 45, 0, 0, 0],
#      [67, 45, 0, 16, 29, 0],
#      [0, 0, 16, 0, 30, 50],
#      [0, 0, 29, 30, 0, 11],
#      [44, 0, 0, 50, 11, 0]]
#
# A = 3
# B = 1
# c = [4, 10, 7, 6, 12, 8]
# D = 80

G = [[(1, 4), (2, 7)],
     [(0, 4), (2, 3), (3, 5)],
     [(0, 7), (1, 3), (3, 4)],
     [(1, 5), (2, 4), (4, 6)],
     [(3, 6)]]
G = [[0, 4, 7, 0, 0],
     [4, 0, 3, 5, 0],
     [7, 3, 0, 4, 0],
     [0, 5, 4, 0, 6],
     [0, 0, 0, 0, 6]]
D = 7

c = [8, 5, 3, 2, 1]
print(cheap(G, 0, len(G) - 1, D, c))