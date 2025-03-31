# There is a list of triples on the boards in the exchange office (currency_1, currency_2, exchange_rate).
# Each of those triples means that exchange office will buy n of currency_2 at the rate of
# n*currency_1.
#   1) Find the most advantageous sequence for converting currency A to currency B.
#   2) Is there such a sequence of currency exchange that starts and ends in the same currency and
# we ends up with more money than we started?
inf = float('inf')

def relax(G, u, v, l, d, parent, i):
    if d[v] < d[u] * l:
        d[v] = d[u] * l
        if parent[v] == u and i != 0:
            return True
        parent[v] = u
    return False

def currency_exchange(G, a, b):
    max_vertex = 0
    for i in range(len(G)):
        max_vertex = max(max_vertex, G[i][0], G[i][1])
    n = len(G)
    d = [0 for _ in range(max_vertex + 1)]
    parent = [None for _ in range(max_vertex + 1)]
    d[a] = 1
    flag = False
    for i in range(max_vertex - 1):
        for u, v, l in G:
            flag = (flag or relax(G, u, v, l, d, parent, i))

    tab = []
    ind = b
    while ind != a:
        tab.append(ind)
        ind = parent[ind]
    tab.append(a)

    return flag, tab[::-1]


G = [(0, 1, 4.5),
     (0, 2, 4),
     (2, 0, 0.25),
     (1, 2, 0.75),
     (3, 2, 10),
     (0, 3, 0.4),
     (1, 4, 6),
     (3, 4, 2)]

a = 0
b = 4
print(currency_exchange(G, a, b))