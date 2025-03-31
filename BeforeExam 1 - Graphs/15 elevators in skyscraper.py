# The skyscraper has 7 floors and n elevators, but there are no stairs. Each elevator has a list of
# the floors it travels to and the speed in seconds per floor. We are on the i floor and we want to get
# to the j floor. What is the minimum time in seconds that we have to spend in elevators to get there?
from queue import PriorityQueue
inf = float('inf')

def relax(u, v, l, d, parent, q):
    if d[v] > d[u] + l:
        d[v] = d[u] + l
        parent[v] = u
        q.put((d[v], v))

def elevators_in_skyscraper(G, s, t):
    n = len(G)
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    q = PriorityQueue()
    d[s] = 0
    q.put((d[s], s))
    while not q.empty():
        du, u = q.get()
        if du == d[u]:
            l = G[u][1]
            for v in G[u][0]:
                relax(u, v, l, d, parent, q)
    return d[t]

floors = [[[1, 2], 3],
          [[3, 4, 5], 5],
          [[3, 5, 6], 2],
          [[4], 3],
          [[5], 1],
          [[6], 4],
          [[], inf]]
print(elevators_in_skyscraper(floors, 0, 5))