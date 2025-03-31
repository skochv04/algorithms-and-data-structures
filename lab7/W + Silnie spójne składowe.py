#directed

def change_direction(G):
    n = len(G)
    M = [[] for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            M[j].append(i)
    return M

def strongly_connected(G):
    n = len(G)
    visited = [False for _ in range(n)]

    def DFS_res(G, u):
        visited[u] = True
        print(u, end=" ")
        for v in G[u]:
            if not visited[v]:
                DFS_res(G, v)

    def DFS_visit(G, u):
        nonlocal tab
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_visit(G, v)
        tab.append(u)

    tab = []

    for u in range(n):
        if not visited[u]:
            DFS_visit(G, u)

    G = change_direction(G)
    visited = [False for _ in range(n)]

    while len(tab):
        u = tab.pop()
        if not visited[u]:
            DFS_res(G, u)
            print("")

G = [[1],
     [2],
     [0, 3, 8],
     [4, 6],
     [5],
     [3],
     [5],
     [8],
     [9],
     [5, 10],
     [7]]

G1 = [[],
      [2],
      [3],
      [6],
      [],
      [0, 1, 4, 6],
      [1]]

strongly_connected(G1)