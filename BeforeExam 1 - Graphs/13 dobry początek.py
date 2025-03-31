#Wierzchołek v w grafie skierowanym nazywamy tak zwanym dobrym początkiem, jeżeli każdy inny wieszchołek można
#osiągnąć ścieżką skierowaną wychodzącą z v. Podać algorytm, który dla podanego grafu stwierdza czy G posiada dobry
#początek; lista sąsiedztwa

def change_direction(G):
    n = len(G)
    M = [[G[j][i] for j in range(n)] for i in range(n)]
    return M

def strongly_connected(G):
    n = len(G)
    visited = [False for _ in range(n)]

    def DFS_res(G, u):
        visited[u] = True
        scc[-1].append(u)
        for v in range(n):
            if G[u][v] and not visited[v]:
                DFS_res(G, v)

    def DFS_visit(G, u):
        nonlocal tab
        visited[u] = True
        for v in range(n):
            if G[u][v] and not visited[v]:
                DFS_visit(G, v)
        tab.append(u)

    tab = []
    scc = []
    for u in range(n):
        if not visited[u]:
            DFS_visit(G, u)

    G = change_direction(G)
    visited = [False for _ in range(n)]

    while len(tab):
        u = tab.pop()
        if not visited[u]:
            scc.append([])
            DFS_res(G, u)
            if len(scc[-1]) < 2:
                scc.pop()
            else:
                scc[-1] = scc[-1][::-1]
    return scc

def wider(G):
    n = len(G)
    for i in range(n):
        G[i].append(0)
    G.append([0 for _ in range(n + 1)])
    return G

def delete_scc(G, component):
    n = len(G)
    for i in range(len(component) - 1):
        G[component[i]][component[i+1]] = 0
    G[component[-1]][component[0]] = 0

    for el in component:
        for i in range(n):
            if G[el][i]:
                G[n-1][i] = 1
                G[el][i] = 0
            if G[i][el]:
                G[i][n-1] = 1
                G[i][el] = 0
    return G

def topsort(G, vis):
    n = len(G)
    visited = [False for _ in range(n)]

    def DFS_visit(G, u):
        visited[u] = True
        for v in range(len(G)):
            if G[u][v] and not visited[v]:
                DFS_visit(G, v)
        if vis[u]:
            tab.append(u)

    tab = []
    for u in range(len(G)):
        if not visited[u]:
            DFS_visit(G, u)
    return tab[::-1]

def check_first(G):
    scc = strongly_connected(G)
    for component in scc:
        G = wider(G)
        delete_scc(G, component)
    n = len(G)
    vis = [True for _ in range(n)]
    for component in scc:
        for i in component:
            vis[i] = False
    # print(*G, sep='\n')
    tab = topsort(G, vis)
    connect = [not vis[i] for i in range(n)]
    connect[tab[0]] = True
    for i in range(len(tab)):
        for j in range(1, len(tab)):
            connect[tab[j]] = connect[tab[j]] or bool(G[tab[i]][tab[j]])
    for i in range(n):
        if not connect[i]:
            return None
    return tab[0]

E = [(0, 1), (1, 2), (3, 2), (2, 4), (4, 1), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 6)]

G2 = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 0, 0, 0, 0, 0], #(3, 0)
      [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

G1 = [[0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0, 0],
      [1, 1, 0, 0, 1, 0, 1],
      [0, 1, 0, 0, 0, 0, 0]]

print(check_first(G1))