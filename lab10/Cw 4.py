#Skojarzenie w grafie: graf dwudzielny, każdy podzbiór krawędzie, które się nie stykają
#Znaleźć skojarzenie w drzewie - graf dwudzielny - na każdym poziomie "zmienia się kolor"

from queue import Queue

def find_path(G, s, t):
    n = len(G)
    q = Queue()
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    visited[s] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.put(v)
    tab = None
    if parent[t] != None:
        ind = t
        tab = []
        while ind != parent[s]:
            tab.append(ind)
            ind = parent[ind]
        tab = tab[::-1]
    return tab

def BFS(G):
    n = len(G)
    q = Queue()
    odd = [-1 for _ in range(n)]
    odd[0] = 0
    q.put(0)
    while not q.empty():
        u = q.get()
        for v in G[u]:
            if odd[v] == -1:
                odd[v] = 1 - odd[u]
                q.put(v)
    left = []
    right = []
    for i in range(n):
        if odd[i] == 1:
            left.append(i)
        elif odd[i] == 0:
            right.append(i)
    return left, right

def ford_fulkerson(G, s, t):
    n = len(G)
    count = 0
    my_path = find_path(G, s, t)
    while my_path:
        count += 1
        for i in range(len(my_path) - 1):
            G[my_path[i]].remove(my_path[i+1])
            G[my_path[i+1]].append(my_path[i])
        my_path = find_path(G, s, t)
    return count


def skojarzenie(G):
    left, right = BFS(G)
    n = len(G)
    G.append([])
    G.append([])
    for el in left:
        G[n].append(el)
    for el in right:
        G[el].append(n+1)
    return ford_fulkerson(G, n, n+1)

G = [[1, 2, 6],
     [0, 5],
     [0],
     [4, 6],
     [3],
     [1],
     [0, 3]]

print(skojarzenie(G))
