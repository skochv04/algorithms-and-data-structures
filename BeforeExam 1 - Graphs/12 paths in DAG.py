# We get as input a directed acyclic graph (DAG - Directed Acyclic Graph) as a list of edges and pair
# of vertices s and t. Find how many possible paths is between s and t.

def make_graph(edges):
    n = len(edges)
    max_vertex = 0
    for i in range(n):
        max_vertex = max(max_vertex, max(edges[i]))
    G = [[] for _ in range(max_vertex + 1)]
    for i in range(n):
        G[edges[i][0]].append(edges[i][1])
    return G

def paths_in_DAG(edges, start, end):
    G = make_graph(edges)

    def DFS_visit(G, u):
        visited[u] = True
        for v in G[u]:
            DP[v] += 1
            DFS_visit(G, v)

    n = len(G)
    visited = [False for _ in range(n)]
    DP = [0 for _ in range(n)]
    DFS_visit(G, start)
    print(DP)
    return DP[end]

edges = [[0, 1], [1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [3, 5], [4, 6], [6, 5]]
start = 1
end = 4
print(paths_in_DAG(edges, start, end))