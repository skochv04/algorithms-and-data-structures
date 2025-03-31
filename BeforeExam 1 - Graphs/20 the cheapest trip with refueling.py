# We are given a graph, in which the vertices are cities and the edges are roads between them. We know
# the fuel price in per liter for each city and the length in kilometers for each road. Our car has
# a D liter tank and burns one liter per kilometer. We start from a with an empty tank. What is
# the minimum cost that we have to pay for fuel to get to the b?

from queue import PriorityQueue
inf = float('inf')

def relax(G, v, u, l, cost):
    for i in range(l, len(G[v])):
        for j in range(i - l, len(G[v])):
            G[v][j] = min(G[v][j], G[u][i] + j * cost)

def road(G, a, b, D):
    DP = [[inf for _ in range(D + 1)] for _ in range(len(G))]
    for i in range(len(DP[0])):
        DP[0][i] = i * G[0][1]
    queue = PriorityQueue()
    queue.put((0, a))
    visited = [False for _ in range(len(G))]
    while not queue.empty():
        d, u = queue.get()
        for v, l in G[u][0]:
            if not visited[v] and D - l >= 0:
                relax(DP, v, u, l, G[v][1])
                queue.put((DP[v][l], v))
        visited[u] = True
    return DP[b][0]

G = [[[(1, 4), (2, 7)], 8],
     [[(0, 4), (2, 3), (3, 5)], 5],
     [[(0, 7), (1, 3), (3, 4)], 3],
     [[(1, 5), (2, 4), (4, 6)], 2],
     [[(3, 6)], 1]]
D = 7

print(road(G, 0, len(G) - 1, D))