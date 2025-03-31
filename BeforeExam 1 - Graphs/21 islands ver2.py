# A certain land consists of islands between which there are air, ferry and bridge connections.
# There is at most one type of connection between two islands. The cost of the overflight from
# island to island costs 8B, ferry crossing costs 5B and for bridge crossing you have to pay 1B.
# Find route from island A to island B which on each subsequent island changes the transport
# to a different one and minimizes the cost of the trip. We are given an array G that specifies
# the cost of connections between the islands. Value 0 means that there is no direct connection.
# Implement islands(G, A, B) function that returns the minimum travels cost from island A
# to island B. If such a route doesn't exist, the function should return None.

from queue import PriorityQueue
from math import inf

def relax(d, u, v, l, queue):
    if l == 1:
        if d[v][1] > d[u][0] + l:
            d[v][1] = d[u][0] + l
            queue.put((d[v][1], v))
        if d[v][2] > d[u][0] + l:
            d[v][2] = d[u][0] + l
            queue.put((d[v][2], v))
    elif l == 5:
        if d[v][0] > d[u][1] + l:
            d[v][0] = d[u][1] + l
            queue.put((d[v][0], v))
        if d[v][2] > d[u][1] + l:
            d[v][2] = d[u][1] + l
            queue.put((d[v][2], v))
    else:
        if d[v][0] > d[u][2] + l:
            d[v][0] = d[u][2] + l
            queue.put((d[v][0], v))
        if d[v][1] > d[u][1] + l:
            d[v][1] = d[u][1] + l
            queue.put((d[v][1], v))


def islands(G, A, B):
    n = len(G)
    d = [[inf for _ in range(3)] for _ in range(n)]
    for i in range(3):
        d[A][i] = 0
    queue = PriorityQueue()
    queue.put((0, A))
    while not queue.empty():
        dist, u = queue.get()
        for v in range(n):
            if G[u][v]:
                relax(d, u, v, G[u][v], queue)
    print(d)
    return min(d[B])

G = [[0, 5, 1, 8, 0, 0, 0],
     [5, 0, 0, 1, 0, 8, 0],
     [1, 0, 0, 8, 0, 0, 8],
     [8, 1, 8, 0, 5, 0, 1],
     [0, 0, 0, 5, 0, 1, 0],
     [0, 8, 0, 0, 1, 0, 5],
     [0, 0, 8, 1, 0, 5, 0]]

print(islands(G, 0, 6))