#Stas Kochevenko
#Opis:

from zad4testy import runtests
from collections import deque
def BFS(G, x, y):
    q = deque()
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    q.append(x)
    visited[x] = True
    while len(q):
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                visited[v] = True
                q.append(v)
    l = 1
    ind = y
    tab = []
    if parent[ind] != None:
        while (parent[ind] != x):
            tab.append((parent[ind], ind))
            l += 1
            ind = parent[ind]
        tab.append((parent[ind], ind))
        return l, tab
    return None

def longer( G, s, t ):
    b = BFS(G, s, t)
    if b != None:
        l = b[0]
        tab = b[1]
        n = len(G)
        for i in tab:
            G[i[0]].remove(i[1])
            G[i[1]].remove(i[0])
            k = BFS(G, s, t)
            if k == None or k[0] > l:
                return i
            G[i[0]].append(i[1])
            G[i[1]].append(i[0])
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
# G = [[1, 4],
#      [0, 2],
#      [1, 3],
#      [2, 5],
#      [0, 5],
#      [4, 3]]
# s = 0
# t = 2
#
# print(longer(G, s, t))