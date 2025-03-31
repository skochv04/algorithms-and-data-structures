#Sprawdzenie czy graf jest dwudzielny. (na macierzy)
from collections import deque

def dwudzielny(T):
    q = deque()
    n = len(T[0])
    vis = [False] * n
    odd = [-1] * n
    q.append(T[0])
    vis[0] = True
    odd[0] = 0
    while len(q):
        u = q.popleft()
        for v in range(n):
            if T[u][v]:
                if not vis[v]:
                    vis[v] = True
                    odd[v] = 1 - odd[u] #zamieniamy 1 na 0 oraz 0 na 1
                    q.append(v)
                elif odd[v] == odd[u]:
                    return False
    return True
        