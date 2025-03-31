# Little town Nsk consists of n junctions connected by m bidirectional roads. Each road connects two
# distinct junctions and no two roads connect the same pair of junctions. It is possible to get from
# any junction to any other junction by these roads. The distance between two junctions is equal to
# the minimum possible number of roads on a path between them. In order to improve the transportation
# system, the city council asks mayor to build one new road. The problem is that the mayor has just
# bought a wonderful new car and he really enjoys a ride from his home, located near junction s to
# work located near junction t. Thus, he wants to build a new road in such a way that the distance
# between these two junctions won't decrease. You are assigned a task to compute the number of pairs
# of junctions that are not connected by the road, such that if the new road between these two
# junctions is built the distance between s and t won't decrease.

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
        for v in range(n):
            if G[u][v] and not visited[v]:
                d[v] = d[u]+1
                parent[v] = u
                visited[v] = True
                q.append(v)
    return d

def fight_against_traffic(n, m, s, t, T):
    G = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        u, v = T[i]
        G[u][v] = 1
        G[v][u] = 1
    distance_s = BFS(G, s)
    distance_t = BFS(G, t)
    print(distance_s)
    print(distance_t)
    D = distance_s[t]
    not_connected_junctions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if not G[i][j] and distance_s[i] + distance_t[j] + 1 >= D and distance_s[j] + distance_t[i] + 1 >= D:
                not_connected_junctions += 1
    return not_connected_junctions

n = 7
m = 7
s = 1
t = 5
T = [(0, 5), (1, 2), (1, 3), (1, 6), (4, 5), (3, 4), (6, 4)]
print(fight_against_traffic(n, m, s, t, T))