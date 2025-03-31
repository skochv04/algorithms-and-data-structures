# The diameter of tree is the distance between its d that distance from each other is
# the most. Find algorithm that, assuming a tree (not necessary a binary) presented as a list
# of edges will return its diameter.

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

def diameter(edges):
    G = make_graph(edges)
    n = len(G)
    d = [0 for _ in range(n)]
    visited = [False for _ in range(n)]

    def DFS_visit(G, u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                d[v] = d[u] + 1
                DFS_visit(G, v)

    DFS_visit(G, 0)
    max_vert = max(d)
    ind = -1
    for i in range(n):
        if d[i] == max_vert:
            ind = i

    d = [0 for _ in range(n)]
    visited = [False for _ in range(n)]

    DFS_visit(G, ind)
    return max(d)

edges = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [4, 9], [5, 10], [7, 11],
         [7, 12], [7, 13], [8, 14], [8, 15], [11, 16], [11, 17], [13, 18], [16, 19], [19, 20]]
print(diameter(edges))