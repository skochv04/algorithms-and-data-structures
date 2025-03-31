def DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    def DFS_visit(G, u):
        nonlocal time, tab
        time += 1
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS_visit(G, v)
        time += 1
        tab.append(u) #topsort

    time = 0
    tab = [] #topsort
    for u in range(len(G)):
        if not visited[u]:
            if u > 0:
                print("Nie jest dwudzielny")
            DFS_visit(G, u)
    return visited, parent, tab[::-1]


G = [[1, 3],
     [3],
     [],
     [2]]

G1 = [[1, 2], [2, 4], [], [], [3, 5], [], [4]]
G2 = [[],
      [],
      [],
      [],
      [],
      [0, 4, 7],
      [],
      []]
for i in range(len(G)):
    print(i, G[i])
print(DFS(G2))