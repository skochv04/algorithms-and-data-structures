# Given a list of edges of the tree (not necessary binary) and highlighted vertex - the root.
# Each vertex creates its own sub-tree. For each vertex, find the number of vertices in its subtree.

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


def subtree_size(edges):
    G = make_graph(edges)
    n = len(G)
    visited = [False for _ in range(n)]
    vertices = [0 for _ in range(n)]

    def DFS_visit (G, u):
        visited[u] = True
        if len(G[u]) == 1:
            vertices[u] += 1
        for v in G[u]:
            if not visited[v]:
                DFS_visit(G, v)
                count = 0
                for i in G[u]:
                    if visited[i]:
                        count += 1
                if count == len(G[u]):
                    for i in G[u]:
                        if vertices[i] > 0:
                            vertices[u] += vertices[i]
                    vertices[u] += 1
    DFS_visit(G, 0)
    return vertices

edges = [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [5, 11], [5, 12], [7, 13],
         [7, 14], [8, 15], [9, 16], [9, 17], [11, 18], [11, 19], [11, 20], [12, 21]]
print(subtree_size(edges))