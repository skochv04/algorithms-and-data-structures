def Euler(G):
    n = len(G)
    for i in range(n): #warunek konieczny
        if len(G[i]) % 2 != 0:
            return False
    visited = [False for _ in range(n)]
    visited_edge = [[False for _ in range(n)] for _ in range(n)]
    last = [0 for _ in range(n)]

    def DFS_visit(G, u):
        nonlocal tab
        visited[u] = True
        for i in range(last[u], len(G[u])):
            v = G[u][i]
            if not visited_edge[u][v]:
                visited[u], visited[v] = True, True
                visited_edge[u][v], visited_edge[v][u] = True, True
                last[u] = i
                DFS_visit(G, v)
        tab.append(u)

    tab = []
    DFS_visit(G, 0)
    for i in range(n): #чи всі відвідані
        if not visited[i]:
            return False
    return tab

G = [[1, 2],
     [0, 2, 3, 4, 5, 6],
     [0, 1, 3, 4, 5, 6],
     [1, 2, 4, 5],
     [1, 2, 3, 5],
     [1, 2, 3, 4],
     [1, 2]]

print(Euler(G))