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
    if parent[ind] != None:
        while (parent[ind] != x):
            l += 1
            ind = parent[ind]
        return l
    return None

def longer( G, s, t ):
    l = BFS(G, s, t)
    if l != None:
        n = len(G)
        for i in range(n):
            for j in range(len(G[i])):
                el = G[i][j]
                G[i].pop(j)
                G[el].remove(i)
                k = BFS(G, s, t)
                if k == None or k > l:
                    return (i, el)
                G[el].append(i)
                G[i].append(el)
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