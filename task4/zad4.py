# 1. Uruchamiam BFS, który zwraca tablice parent i distance od s.
# 2. Jeżeli wierzchołek t ma dokładnie jednego sąsiada z najmniejszą odległością do s,
# to usunięcie łączącej je krawędzi na pewno wydłuży najkrótszą ścieżkę.
# W przeciwnym razie zapisuję ścieżkę po parent i idąc inną równie krótką ścieżką
# szukam wierzchołka spotkania tych ścieżek.
# 3. Jeżeli tym wierzchołkiem jest s, to te ścieżki są niezależne i tak samo najkrótsze,
# a więc można zwrócić None.
# W przeciwnym razie ustawiam t na wierzchołek spotkania i powtarzam od kroku 2.


from zad4testy import runtests

from collections import deque

def BFS(G, s):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [-1 for _ in range(n)]
    Q = deque()
    d[s] = 0
    Q.append(s)
    visited[s] = True
    while len(Q):
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
                Q.append(v)
    return d, parent

def longer( G, s, t ):
    n = len(G)
    d, parent = BFS(G, s)
    while t != s:
        dist = d[parent[t]]
        alt = None
        for i in G[t]:
            if d[i] == dist and i != parent[t]:
                alt = i
        if not alt:
            return parent[t], t
        path = [False for _ in range(n)]
        p = parent[t]
        while p != parent[s]:
            path[p] = True
            p = parent[p]
        p = alt
        while not path[p]:
            p = parent[p]
        if p == s:
            return None
        t = p


G = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(longer(G, 0, 2))
#zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( longer, all_tests = True )