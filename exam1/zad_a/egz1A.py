#Stas Kochevenko
#Opis: W danym algorytmie na początku budujemy nowy graf, w którym wszystkie krawędzie będą mieli wagi "po napadzie"
#złycerza, a następnie urochamiamy algorytm Dijkstry dwa razy, zapisując wyniki: pierwszy - to szukanie najmniejszego
#kosztu dotarcia do każdego wierzchołka w oryginalnym grafie z s, a drugi - koszt dotarcia do każdego wierzchołka z t w
#tym nowym grafie. Następnie, dla każdego wierzchołka będziemy próbować zabrać całe jego złoto, więc koszt całej ścieżki
#będzie wynosił koszt dotarcia do tego wierzchołka z s minus zabrane złoto plus koszt dotarcia do t z tego wierzchołka
#przy założeniu, że już wykorzystaliśmy możliwość zabrania złota. Wynik końcowy to minimum z tych wszyszkich możliwości.
#Złożoność to ElogV + V + (2 * ElogV) = ElogV = V^2logV.

from egz1Atesty import runtests
from queue import PriorityQueue
inf = float('inf')

def relax(u, v, l, d, parent, q):
  if d[v] > d[u] + l:
    d[v] = d[u] + l
    parent[v] = u
    q.put((d[v], v))

def Dijkstry(G, s):
  n = len(G)
  parent = [None for _ in range(n)]
  d = [inf for _ in range(n)]
  q = PriorityQueue()
  d[s] = 0
  q.put((d[s], s))
  while not q.empty():
    du, u = q.get()
    if d[u] == du:
      for v, l in G[u]:
        relax(u, v, l, d, parent, q)
  return d

def newgraph(G, r):
  n = len(G)
  M = [[] for _ in range(n)]
  for u in range(n):
    for v, l in G[u]:
      M[u].append((v, l * 2 + r))
  return M

def gold(G,V,s,t,r):
  n = len(G)
  M = newgraph(G, r)
  d1 = Dijkstry(G, s)
  d2 = Dijkstry(M, t)
  mini = d1[t]
  for u in range(n):
    mini = min(mini, d1[u] - V[u] + d2[u])
  return mini

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
