# Public transport in a certain city is quite strangely organized. There is a separate charge for
# each section between two stations. However, the total d incurred from the s of the journey
# is subtracted from this amount (if it is negative you just pay nothing). We are given a connection
# graph in any representation (undirected, weighted). Find the minimum d of driving this route.
from queue import PriorityQueue
inf = float('inf')

def relax(u, v, l, d):
    if l - d[u] > 0 and d[v] > l:
        d[v] = l
        return True
    elif l - d[u] < 0 and d[v] > d[u]:
        d[v] = d[u]
        return True
    return False


def weird_fees(G, s):
    n = len(G)
    queue = PriorityQueue()
    d = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    d[s] = 0
    queue.put((d[s], s))
    while not queue.empty():
        du, u = queue.get()
        for v, l in G[u]:
            if not visited[v] and relax(u, v, l, d):
                queue.put((d[v], v))
        visited[u] = True
    return d

G =     [[(1, 60), (3, 120), (4, 40)],
         [(0, 60), (2, 80)],
         [(1, 80), (4, 100), (7, 70)],
         [(0, 120), (6, 150)],
         [(0, 40), (2, 100), (5, 90)],
         [(4, 90), (6, 60)],
         [(3, 150), (5, 60), (7, 90)],
         [(2, 70), (6, 90)]]
print(weird_fees(G, 0))