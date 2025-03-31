# A famous professor invited you to a meeting in the Magic City. In this city some roads can only be used
# by people under the age of 30 (including us), others only by people over the age of 30 (including the
# professor). There are also roads that can be traveled by anyone. Each road has a certain length,
# expressed in a positive natural number, and roads can be one-way or two-way. These roads connect possible
# meeting locations. Among them, we distinguish your house and the professor's house. The professor asks
# us to choose a place for the meeting so that the total distance that we and the professor must travel
# is the smallest. If there is more than one such a place, list them all. If there is no such a place,
# the algorithm should consider that.
from queue import PriorityQueue
inf = float('inf')

def make_graph(under_thirty, over_thirty, normal):
    max_vertex = 0
    for i in range(len(under_thirty)):
        max_vertex = max(max_vertex, max(under_thirty[i]))
    for i in range(len(over_thirty)):
        max_vertex = max(max_vertex, max(over_thirty[i]))
    for i in range(len(normal)):
        max_vertex = max(max_vertex, max(normal[i]))

    G = [[] for _ in range(max_vertex + 1)]

    for u, v, w in under_thirty:
        G[u].append(('Y', v, w))
        G[v].append(('Y', u, w))

    for u, v, w in over_thirty:
        G[u].append(('O', v, w))
        G[v].append(('O', u, w))

    for u, v, w in normal:
        G[u].append(('A', v, w))
        G[v].append(('A', u, w))
    return G

def relax(u, v, l, d, q):
    if d[v] > d[u] + l:
        d[v] = d[u] + l
        q.put((d[v], v))

def Dijkstra(G, s, t, person):
    n = len(G)
    d = [inf for _ in range(n)]
    q = PriorityQueue()
    d[s] = 0
    q.put((d[s], s))
    while not q.empty():
        du, u = q.get()
        if d[u] == du:
            for p, v, l in G[u]:
                if p == 'A' or p == person:
                    relax(u, v, l, d, q)
    return d

def meeting_with_the_professor(under_thirty, over_thirty, normal, student_house, professor_house):
    G = make_graph(under_thirty, over_thirty, normal)
    # print(*G, sep='\n')
    d1 = Dijkstra(G, student_house, professor_house, 'Y')
    d2 = Dijkstra(G, professor_house, student_house, 'O')
    mini = inf
    n = len(G)
    for i in range(n):
        if d1[i] != inf and d2[i] != inf:
            if abs(d1[i] - d2[i]) < mini:
                mini = min(mini, abs(d1[i] - d2[i]))
                vertics = i
    tab = [vertics]
    for i in range(n):
        if d1[i] != inf and d2[i] != inf:
            if abs(d1[i] - d2[i]) == mini and i != vertics:
                tab.append(i)
    return tab

under_thirty = [(0, 2, 2), (0, 4, 4), (1, 3, 1), (3, 7, 4), (8, 10, 5), (11, 12, 1)]
over_thirty = [(0, 1, 3), (0, 11, 4), (5, 6, 2), (6, 11, 2), (7, 8, 2), (9, 10, 2)]
normal = [(0, 3, 3), (2, 3, 5), (4, 5, 3), (7, 9, 1), (6, 9, 3), (10, 12, 4)]
student_house = 0
professor_house = 12
print(meeting_with_the_professor(under_thirty, over_thirty, normal, student_house, professor_house))