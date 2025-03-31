# Let's imagine an underground labyrinth composed of huge caves connected by narrow corridors. In one
# of caves, the dwarves have built their settlement and each of the other caves has a number of trolls.
# The dwarves want to plan their defense in case of being attacked by trolls. They intend to sneak in
# and plant an explosive load in one of the corridors, so that the trolls living beyond this corridor
# have no path to reach the dwarven settlement. Which of the corridors should be blown up to cut off
# trolls' access to the dwarven settlement.

from collections import deque
from queue import Queue
inf = float('inf')

def BFS(G, trolls, start, s, t):
    queue = Queue()
    queue.put(t)
    visited = [False] * len(G)
    visited[t] = True
    visited[s] = True
    trolls_number = trolls[t]
    while not queue.empty():
        u = queue.get()
        for v in G[u]:
            if not visited[v]:
                trolls_number += trolls[v]
                queue.put(v)
                visited[v] = True
    return trolls_number


def bridges(G, s):
    n = len(G)
    d = [inf for _ in range(n)]
    low = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    def DFS_visit(G, u):
        nonlocal time
        visited[u] = True
        d[u] = time
        low[u] = time
        time += 1
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS_visit(G, v)
                low[u] = min(low[u], low[v])
                # if low[v] > d[u]:
                #     tab.append((u, v))
            elif v != parent[u]: #krawędż wstęczna
                low[u] = min(low[u], d[v])

    time = 0
    tab = []
    for u in range(n):
        if not visited[u]:
            DFS_visit(G, u)
    for i in range(n):
        if d[i] == low[i] and parent[i] is not None:
            tab.append((parent[i], i))
    return tab


def dwarves_and_trolls(G, trolls, s):
    all = bridges(G, s)
    coridor, max_trolls = 0, 0
    for bridge in all:
        loc = BFS(G, trolls, s, bridge[0], bridge[1])
        if loc == inf:
            loc = BFS(G, trolls, s, bridge[1], bridge[0])
        if loc > max_trolls:
            max_trolls = loc
            coridor = (bridge[0], bridge[1])
    return coridor

G = [[1, 2, 3, 4], [0, 2, 5, 6], [0, 1, 3], [0, 2], [0, 9, 10], [1, 7, 8],
         [1], [5, 8], [5, 7], [4, 10], [4, 9, 11], [10]]
trolls = [1, 2, 8, 7, 17, 4, 13, 3, 12, 3, inf, 11]
print(dwarves_and_trolls(G, trolls, 10))