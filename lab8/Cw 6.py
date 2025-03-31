#1$ = 1,2 Євро
#Бейльман Форд, чи є цикл о від'ємній вазі, перевірити чи під час обміну
#може вдасться обміняти менше (1 зл) на більші (1,2 зл)

from math import inf
from math import log

def relax(u, v, l, d, parent):
    if d[v] > d[u]+l:
        d[v] = d[u]+l
        parent[v] = u

def find_more(G, s):
    n = len(G)
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)] #długości najkrótszych ścieżek
    d[s] = 1
    for i in range(n - 1):
        for u in range(n):
            for v in range(n):
                l = log(G[u][v], 2)
                relax(u, v, l, d, parent)
    for u in range(n):
        for v in range(n):
            l = log(G[u][v], 2)
            if d[u] + l < d[v]:
                return None
    return d, parent


#Zł	 $	 ₴	 €	 Kč
G = [[1, 0.24, 8.75, 0.22, 5.13],
     [4.16, 1, 36.43, 0.9, 21.36],
     [0.11, 0.627, 1, 0.025, 0.59],
     [4.63, 1.11, 40.54, 1, 23.76],
     [0.19, 0.047, 1.71, 0.042, 1]]

# G = [[1, 0.24, ],
#      [],
#      []]
# G1 = [[1, 4.5, 4, 0.4, -inf],
#      [-inf, 1, 0.75, -inf, 6],
#      [0.25, -inf, 1, -inf, -inf],
#      [-inf, -inf, 11, 1, 2],
#      [-inf, -inf, -inf, -inf, -inf]]
#
print(find_more(G, 0))