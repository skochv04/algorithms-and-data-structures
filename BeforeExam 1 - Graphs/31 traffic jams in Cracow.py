# There are traffic jams in Cracow during rush hours. Therefore drivers are more concerned with time than
# with the real distance between two points. We are given a map of Cracow, distances and travel times are
# marked between road intersections. There are one-way streets and two-way streets in Cracow. Drivers need
# an app to help them find the roads that allow them to get from intersection A to B in the shortest
# possible time and among those with the shortest time it selects and returns the shortest in terms of
# distance. We have to process Q queries represented as (intersectionA, intersectionB) and answer each of
# them with a pair (time, distance) of the best way. All queries refer to the same graph.
# What solution gives the best complexity in each of the following cases?

from math import inf

def traffic_jams(G):
    n = len(G)
    d = [[(inf, inf) for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if G[u][v]:
                d[u][v] = G[u][v]
        d[u][u] = (0, 0)
    for t in range(n):
        for u in range(n):
            for v in range(n):
                if d[u][t][0] + d[t][v][0] < d[u][v][0] or (d[u][t][0] + d[t][v][0] == d[u][v][0] and d[u][t][1] + d[t][v][1] < d[u][v][1]):
                    d[u][v] = (d[u][t][0] + d[t][v][0], d[u][t][1] + d[t][v][1])
    return d

# (time, distance)
G =     [[0, (3, 2), (4, 1), 0, 0, 0, 0, 0, 0, 0],
         [(3, 2), 0, 0, (2, 3), 0, 0, 0, 0, 0, 0],
         [(4, 1), 0, 0, 0, 0, 0, (2, 5), 0, 0, 0],
         [0, 0, 0, 0, (1, 1), (1, 4), 0, 0, 0, 0],
         [0, 0, 0, (1, 1), 0, 0, 0, (5, 5), 0, 0],
         [0, 0, 0, 0, 0, 0, (6, 1), 0, (3, 3), 0],
         [0, 0, (2, 5), 0, 0, 0, 0, 0, (3, 2), 0],
         [0, 0, 0, 0, (5, 5), 0, 0, 0, 0, (4, 5)],
         [0, 0, 0, 0, 0, 0, (3, 3), 0, 0, (4, 2)],
         [0, 0, 0, 0, 0, 0, 0, (4, 5), (4, 2), 0]]
print(*traffic_jams(G), sep='\n')