#Mamy daną macierz i szukamy najkrótszą ścieżkę od s wierszchołka do d.
#Otworzyć ścieżkę tą.
from collections import deque
def longest(T, s, d):
    n = len(T[0])
    vis = [0] * n
    par = [-1] * n
    kolejka = deque()
    kolejka.append(s)
    vis[s] = 1
    while(len(kolejka)):
        act = kolejka.popleft()
        for i in range(n):
            if(T[act][i] and not vis[i]):
                par[i] = act
                vis[i] = 1
                kolejka.append(i)

    tab = []
    ind = d
    while(par[ind] != s):
        print(ind)
        tab.append(ind)
        ind = par[ind]
    tab.append(ind)
    tab.append(s)

    # while(ind != par[s]):
    #     print(ind)
    #     tab.append(ind)
    #     ind = par[ind]


    tab = tab[::-1]
    return tab


# wyp(prev, s, d)
#     if (d!= s):
#         wyp(prev, s, prev[d])
#     print(d)

G = [[0, 1, 0, 0],
     [0, 0, 0, 1],
     [0, 0, 0, 0],
     [1, 0, 1, 0]]

for i in range(len(G)):
    print(i, G[i])
print(longest(G, 3, 0))