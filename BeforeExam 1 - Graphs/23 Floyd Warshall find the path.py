# Implement the Floyd-Warshall algorithm so that it gives an information that allows the
# reconstruction of the shortest path between any two pairs of vertices over time depending on the
# length of that path.
inf = float('inf')

def Floyd_Warshall(G, a, b):
    n = len(G)
    d = [[inf for _ in range(n)] for _ in range(n)]
    parent = [[None for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if G[u][v] != -1:
                d[u][v] = G[u][v]
                parent[u][v] = u
        d[u][u] = 0
    for t in range(n):
        for u in range(n):
            for v in range(n):
                if d[u][v] > d[u][t]+d[t][v]:
                    d[u][v] = d[u][t]+d[t][v]
                    parent[u][v] = t

    tab = []
    ind = b
    while ind != None:
        tab.append(ind)
        ind = parent[a][ind]
    return tab[::-1]

G =     [[-1, 7, 6, -1, -1, -1, -1, -1, -1],
         [7, -1, -1, 3, 2, -1, -1, -1, -1],
         [6, -1, -1, -1, -1, 2, -1, -1, -1],
         [-1, 3, -1, -1, -1, -1, -1, 4, -1],
         [-1, 2, -1, -1, -1, -1, 1, -1, 15],
         [-1, -1, 2, -1, -1, -1, 3, 4, -1],
         [-1, -1, -1, -1, 1, 3, -1, 6, -1],
         [-1, -1, -1, 4, -1, 4, 6, -1, 5],
         [-1, -1, -1, -1, 15, -1, -1, 5, -1]]

print(Floyd_Warshall(G, 0, 8))