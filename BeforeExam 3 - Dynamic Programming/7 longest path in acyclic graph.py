# Find the longest path in acyclic directed graph (DAG).

def longest(G):
    n = len(G)
    dp = [0 for _ in range(n)]
    visited = [False for _ in range(n)]

    def DFS_visit(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_visit(v)
            dp[u] = max(dp[u], dp[v] + 1)

    for i in range(1, n):
        if not visited[i]:
            DFS_visit(i)
    return max(dp)

G = [[],
     [2, 3],
     [],
     [2],
     [1, 2, 5],
     [2, 3]]

print(longest(G))