# Byteland is a land containing N cities and N-1 two-way roads. The road system creates a consistent
# G. We are given a list of K cities to which we have to deliver packages and being able to start
# and finish the route in any city, find the minimum distance that we must travel to deliver all packages.


def packages_delivery(G, s):
    n = len(G)
    visited = [False for _ in range(n)]
    d = [0 for _ in range(n)]
    parent = [0 for _ in range(n)]

    def DFS_visit(G, u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                d[v] = d[u] + 1
                parent[v] = u
                DFS_visit(G, v)


    parent[s] = -1
    DFS_visit(G, s)

    max_vert = d.index(max(d))

    visited = [False for _ in range(n)]
    d = [0 for _ in range(n)]
    parent = [0 for _ in range(n)]
    parent[max_vert] = -1
    DFS_visit(G, max_vert)

    start = d.index(max(d))
    diameter = [start]
    i = start
    while parent[i] != -1:
        diameter.append(parent[i])
        i = parent[i]
    route = 0
    for j in range(n):
        if j == start:
            continue
        if j not in diameter:
            route += 2
        else:
            route += 1
    return route


G = [[1], [0, 2], [1, 3, 4], [2, 6], [2, 5], [4], [3, 7, 8], [6], [6, 9, 10, 11],
         [8], [8], [8, 12, 16], [11, 13, 14], [12, 15], [12], [13], [11, 17, 18], [16], [16]]
print(packages_delivery(G, 0))