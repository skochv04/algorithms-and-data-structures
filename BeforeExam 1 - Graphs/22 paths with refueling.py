# We are given two-dimensional array G which represents adjacency matrix of the weighted directed
# graph that corresponds to the road map (weights are the distances, the number -1 means that there
# is no edge). In some vertices there are petrol stations, we are given their list P. A full tank of
# f is enough to cover the distance d. When entering the station, the car is always fully refed.
# Implement an algorithm which searches for the shortest possible route from vertex A to vertex B, if
# there is one and returns a list of consecutive visited vertices on the route (we assume that there
# is also a petrol station in vertex A, car can only travel distance d without refing).

from queue import PriorityQueue
inf = float('inf')

def relax(u, v, l, d, f, parent, q):
    if d[v] > d[u] + l:
        d[v] = d[u] + l
        f[v] = f[v] + f[u] - l
        parent[v] = u
        q.put((d[v], f[v], v))

def paths_with_refueling(G, P, D, a, b):
    n = len(G)
    d = [inf for _ in range(n)]
    f = [0 for _ in range(n)]
    for i in P:
        f[i] = D
    parent = [None for _ in range(n)]
    q = PriorityQueue()
    d[a] = 0
    q.put((d[a], f[a], a))
    while not q.empty():
        du, fu, u = q.get()
        if d[u] == du:
            for v in range(n):
                l = G[u][v]
                if l != -1 and fu >= l:
                    relax(u, v, l, d, f, parent, q)
    tab = []
    ind = b
    while ind != None:
        tab.append(ind)
        ind = parent[ind]
    return tab[::-1]


def relaxation(u, v, l, d):
    if d[v] > d[u] + l:
        d[v] = d[u] + l
        return True

def paths_with_refueling2(G, P, D, a, b):
    n = len(G)
    d = [inf for _ in range(n)]
    d[a] = 0
    q = PriorityQueue()
    q.put((d[a], D, a))
    while not q.empty():
        du, loc_d, u = q.get()
        for v in range(n):
            l = G[u][v]
            if l != -1 and loc_d - l >= 0 and relaxation(u, v, l, d):
                if v in P:
                    q.put((d[v], D, v))
                else:
                    q.put((d[v], loc_d - l, v))
    return d


G =     [[-1, 6, -1, 5, 2],
         [-1, -1, 1, 2, -1],
         [-1, -1, -1, -1, -1],
         [-1, -1, 4, -1, -1],
         [-1, -1, 6, -1, -1]]
P = [0, 1, 3]
print(paths_with_refueling(G, P, 5, 0, 2))