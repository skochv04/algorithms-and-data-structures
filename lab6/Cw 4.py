#Є граф, де кожне ребро має цілочисельну вагу, і ваги ребер між собою різні. Алгоритм має перевірити для двох вершин,
#чи існує стежка від x до y, щоб кожне наступне ребро мало меншу вагу.

def DFS(G, x, y):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    a = False

    def DFS_visit(G, u):
        nonlocal a
        if u == y:
            a = True
        visited[u] = True
        for v in range(n):
            if G[u][v] and not visited[v] and (parent[u] == None or G[u][v] < G[parent[u]][u]):
                parent[v] = u
                DFS_visit(G, v)
    DFS_visit(G, x)
    return a


G = [[0, 10, 44, 0],
     [10, 0, 0, 14],
     [44, 0, 0, 8],
     [0, 14, 8, 0]]

print(DFS(G, 0, 3))