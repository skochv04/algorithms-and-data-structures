# Henry the sailor lives on island of an archipelago. All islands including archipelago are so small that
# they can be represented as points in R^2 space. The positions of all islands are given as the sequence
# W = ((x1, y1), ..., (xn, yn)). Henry lives on the island (x1, y1), but he wants to move to the island
# (xn, yn). Normally every day he can sail to an island that is at most Z distance (in standard Euclidean
# distance). He can also sail up to 2Z distance, provided that he will rest all the next day. Henry
# always must stay overnight on some island. Find minimum number of days Henry needs to get to his
# target island (or states that it is impossible).
from math import sqrt
from queue import Queue
inf = float('inf')

def count_distance(point1, point2):
    x = abs(point1[0] - point2[0])
    y = abs(point1[1] - point2[1])
    return sqrt(x ** 2 + y ** 2)

def the_sailor_Henry(W, Z, s):
    N = len(W)
    G = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                distance = count_distance(W[i], W[j])
                if distance <= Z:
                    G[i].append([j, 1])
                elif Z < distance <= 2 * Z:
                    G[i].append([j, 2])
    n = len(G)
    parent = [-1 for _ in range(N)]
    d = [inf for _ in range(N)]
    q = Queue()

    d[s] = 0
    q.put((0, s))

    while not q.empty():
        du, u = q.get()
        if du == d[u]:
            for v, days in G[u]:
                if d[v] > d[u] + days:
                    d[v] = d[u] + days
                    parent[v] = u
                    q.put((d[v], v))
    tab = []
    if d[-1] != inf:
        ind = N - 1
        while ind != -1:
            tab.append(W[ind])
            ind= parent[ind]
        return d[-1], tab[::-1]
    return False

Z = 1
W = [(0, 0), (0, 1), (2, 1), (1, 3), (2, 5), (3, 2), (5, 2), (4, 4), (3, 4), (4, 1), (2, 4), (5, 5)]
print(the_sailor_Henry(W, Z, 0))