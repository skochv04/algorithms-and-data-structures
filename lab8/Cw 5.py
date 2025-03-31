#Wybrać tak, żeby Alice przejechała jak najmniej kilometrów
#   G = (V, E) - połączenia między miastami
#   wagi w E to długości
#   2 kierowców - Alicja i Bob - prowadzą na zmianie
#   S, T - miasto startowe, końcowe
#   Alicja ustala trase - chce najmniej przejechać, wybiera kto pierwszy jedzie


from queue import PriorityQueue
from math import inf


def relax(u, v, l, d, parent, queue, person):
    if d[v] > d[u]+l:
        d[v] = d[u]+l
        parent[v] = u
        queue.put((d[v], v, person))

def trasa(G, s, f):
    n = len(G)

    # Pierwszy jedzie Bob
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    q = PriorityQueue()
    d[s] = 0
    q.put((d[s], s, True))
    while not q.empty():
        du, u, person = q.get()
        if d[u] == du:
            for v, l in G[u]:
                if person:
                    relax(u, v, 0, d, parent, q, False)
                else:
                    relax(u, v, l, d, parent, q, True)
    # print(d, parent)
    szlak = (d[f], "Bob")


    #Pierwsza jedzie Alisia
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    d[s] = 0
    q.put((d[s], s, False))
    while not q.empty():
        du, u, person = q.get()
        if d[u] == du:
            for v, l in G[u]:
                if person:
                    relax(u, v, 0, d, parent, q, False)
                else:
                    relax(u, v, l, d, parent, q, True)
    # print(d, parent)
    if szlak[0] > d[f]:
        szlak = (d[f], "Alisia")
    return szlak


G = [[(1, 1), (8, 2)],
      [(0, 1), (2, 3), (6, 3)],
      [(1, 3), (3, 5)],
      [(2, 5), (4, 1), (6, 2)],
      [(3, 1), (5, 8), (7, 4)],
      [(4, 8), (6, 3), (7, 1)],
      [(1, 3), (3, 2), (5, 3), (8, 1)],
      [(4, 4), (5, 1), (8, 7)],
      [(6, 1), (7, 7), (0, 2)]]

print(trasa(G, 5, 1))