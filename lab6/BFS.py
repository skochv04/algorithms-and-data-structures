from collections import deque

def BFS (G, s):
    q = deque()
    n = len(G)
    d = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    q.append(s)
    d[s] = 0
    visited[s] = True
    while len(q) != 0:
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                d[v] = d[u]+1
                parent[v] = u
                visited[v] = True
                q.append(v)
            # elif v != parent[u]:
            #     print("CYCLE")
    return d, visited, parent

G = [[1],
     [3],
     [],
     [0, 2]]
for i in range(len(G)):
    print(i, G[i])
print(BFS(G, 0))












