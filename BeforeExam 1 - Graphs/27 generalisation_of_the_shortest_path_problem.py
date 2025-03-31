# In addition to length of edges, the graph has vertex costs associated with it. Let us define the
# cost of the path as the sum of the costs of its edges and sum of the costs of the vertices (along
# with the ends). Find the cheapest paths between the starting vertex and all the other vertices.
# Find a solution for directed and undirected graph.

from queue import PriorityQueue
inf = float('inf')

def relax(u, v, l, d, parent, queue):
    if d[v] > d[u]+l:
        d[v] = d[u]+l
        parent[v] = u
        queue.put((d[v], v))

def Dijkstry(G, V, s, t):
    n = len(G)
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    q = PriorityQueue()
    d[s] = V[s]
    q.put((d[s], s))
    while not q.empty():
        du, u = q.get()
        if d[u] == du:
            for v, l in G[u]:
                relax(u, v, l + V[v], d, parent, q)
    return d

def shortest_path_undirected(G, V, s, t):
    return Dijkstry(G, V, s, t)

def Dijkstry2(G, V, s, t):
    n = len(G)
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    q = PriorityQueue()
    d[s] = V[s]
    q.put((d[s], s))
    while not q.empty():
        du, u = q.get()
        if d[u] == du:
            for v in range(n):
                if G[u][v] != 0:
                    l = G[u][v]
                    relax(u, v, l, d, parent, q)
    return d

def shortest_path_directed(G, V, s, t):
    n = len(G)
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                G[i][j] += V[j]
    return Dijkstry2(G, V, s, t)
#
# undirected_graph = [[[1, 4], [2, 3]],
#                     [[0, 4], [3, 6]],
#                     [[0, 3], [3, 1], [4, 4], [6, 20]],
#                     [[1, 6], [2, 1], [5, 3]],
#                     [[2, 4], [6, 5]],
#                     [[3, 3], [6, 5]],
#                     [[2, 20], [4, 5], [5, 5]]]
# undirected_graph_vertices = [5, 4, 1, 2, 5, 4, 3]
# print(shortest_path_undirected(undirected_graph, undirected_graph_vertices, 0, 6))

directed_graph = [[0, 2, 6, 4, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 5, 7, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 2, 0, 0],
                  [0, 0, 0, 0, 0, 2, 0, 0, 5, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
                  [0, 0, 0, 0, 0, 8, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 5, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
directed_graph_vertices = [4, 5, 2, 6, 3, 1, 9, 1, 2, 4]
print(shortest_path_directed(directed_graph, directed_graph_vertices, 0, 9))