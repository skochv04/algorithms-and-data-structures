# A certain land consists of islands between which there are air, ferry and bridge connections.
# There is at most one type of connection between two islands. The cost of the overflight from
# island to island costs 8B, ferry crossing costs 5B and for bridge crossing you have to pay 1B.
# Find route from island A to island B which on each subsequent island changes the transport
# to a different one and minimizes the cost of the trip. We are given an array G that specifies
# the cost of connections between the islands. Value 0 means that there is no direct connection.
# Implement islands(G, A, B) function that returns the minimum travels cost from island A
# to island B. If such a route doesn't exist, the function should return None.
# plane = 8
# ferry = 5
# bridge = 1

from queue import PriorityQueue
inf = float('inf')

def relax(u, v, l, d, parent, q):
    if d[v] > d[u] + l:
        d[v] = d[u] + l
        parent[v] = u
        q.put((d[v], v, l))

def islands(G, a, b):
     # plane = 8
     # ferry = 5
     # bridge = 1
     n = len(G)
     d = [inf for _ in range(n)]
     parent = [None for _ in range(n)]
     q = PriorityQueue()
     d[a] = 0
     transport = None
     q.put((d[a], a, transport))
     while not q.empty():
          du, u, transport = q.get()
          if d[u] == du:
               for v in range(n):
                    l = G[u][v]
                    if l != 0 and l != transport:
                         relax(u, v, l, d, parent, q)
     return d, parent

G = [[0, 5, 1, 8, 0, 0, 0],
     [5, 0, 0, 1, 0, 8, 0],
     [1, 0, 0, 8, 0, 0, 8],
     [8, 1, 8, 0, 5, 0, 1],
     [0, 0, 0, 5, 0, 1, 0],
     [0, 8, 0, 0, 1, 0, 5],
     [0, 0, 8, 1, 0, 5, 0]]

print(islands(G, 0, 5))