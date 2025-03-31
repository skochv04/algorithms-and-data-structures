# In Absurdistan, there are n towns (numbered 1 through n) and m bidirectional railways. There is also
# an absurdly simple road network — for each pair of different towns x and y, there is a bidirectional
# road between towns x and y if and only if there is no railway between them. Travelling to a different
# town using one railway or one road always takes exactly one hour. A train and a bus leave town 1 at
# the same time. They both have the same destination, town n, and don't make any stops on the way
# (but they can wait in town n). The train can move only along railways and the bus can move only along
# roads. You've been asked to plan out routes for the vehicles; each route can use any road/railway
# multiple times. One of the most important aspects to consider is safety — in order to avoid
# accidents at railway crossings, the train and the bus must not arrive at the same town (except
# town n) simultaneously. Under these constraints, what is the minimum number of hours needed for
# both vehicles to reach town n (the maximum of arrival times of the bus and the train)? Note, that bus
# and train are not required to arrive to the town n at the same moment of time, but are allowed to do so.
from queue import Queue

def the_two_routes_1(n, m, edges):
    train = [[0 for j in range(n)] for i in range(n)]
    for u, v in edges:
        train[u][v] = 1
        train[v][u] = 1
    bus = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                bus[i][j] = 1 - train[i][j]

    visited_t = [False for _ in range(n)]
    dt = [-1 for _ in range(n)]
    q = Queue()
    dt[0] = 0
    visited_t[0] = True
    q.put(0)
    while not q.empty():
        u = q.get()
        for v in range(n):
            if train[u][v] and not visited_t[v]:
                dt[v] = dt[u] + 1
                visited_t[v] = True
                q.put(v)

    visited_b = [False for _ in range(n)]
    db = [-1 for _ in range(n)]
    db[0] = 0
    visited_b[0] = True
    q.put(0)
    while not q.empty():
        u = q.get()
        for v in range(n):
            if bus[u][v] and not visited_b[v]:
                if v == n - 1 or dt[v] != db[u] + 1:
                    db[v] = db[u] + 1
                    visited_b[v] = True
                    q.put(v)
    print(dt, db)
    return max(dt[n-1], db[n-1])

def the_two_routes(n, m, edges):
    G = [[0 for j in range(n)] for i in range(n)]
    for u, v in edges:
        G[u][v] = G[v][u] = 1
    if G[0][n-1] == 1:
        for i in range(n):
            for j in range(n):
                if i != j:
                    G[i][j] = 1 - G[i][j]

    visited = [False for _ in range(n)]
    d = [-1 for _ in range(n)]
    q = Queue()
    d[0] = 0
    visited[0] = True
    q.put(0)
    while not q.empty():
        u = q.get()
        for v in range(n):
            if G[u][v] and not visited[v]:
                d[v] = d[u] + 1
                visited[v] = True
                q.put(v)
    return d[n-1]

n = 5
m = 5
edges = [(0, 1), (1, 3), (1, 4), (3, 4)]
print(the_two_routes(n, m, edges))