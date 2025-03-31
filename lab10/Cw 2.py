#Lista fabryk, lista skupów...
# Mamy dany graf skierowany G = (V, E) oraz funkcję c: E → N opisującą przepustowość każdej krawędzi
# (liczbę jednostek towaru na godzinę, które mogą się przemieszczać krawędzią). Poza tym mamy dany zbiór
# wierzchołków-fabryk S = {s1, ..., sn} oraz zbiór wierzchołków-sklepów T = {t1, ..., tm}. Dla każdej
# fabryki s[i] znamy liczbę p[i] określającą ile jednostek towaru na godzinę fabryka może maksymalnie
# produkować. Jednocześnie dla każdego sklepu t[j] mamy liczbę q[j], która mówi ile jednostek towaru
# na godzinę musi do tego sklepu docierać. Proszę podać algorytm, który sprawdza, czy da się zapewnić,
# żeby do każdego sklepu docierało z fabryk dokładnie tyle jednostek towaru ile sklep wymaga
# jednocześnie nie zmuszając żadnej fabryki do przekroczenia swoich możliwości produkcyjnych i nie
# przekraczając przepustowości żadnej z krawędzi.

from copy import deepcopy
#sources = list(tuple[inf, inf]) #v, w
def modify_problem(G, sources, sinks):
    new = deepcopy(G)
    n = len(G)
    new.append([0 for _ in range(n)])
    new.append([0 for _ in range(n)])
    for i in range(n+2):
        new.extend([0, 0])
    for v, w in sources:
        new[n][v] = w
    for v, w in sinks:
        new[v][n+1] = w
    return ford_fulkerson(new, n, n+1)


graph = [[0, 10, 0, 8, 0, 0, 0],
         [0, 0, 11, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 9, 0],
         [0, 5, 0, 0, 6, 0, 0],
         [0, 0, 0, 0, 0, 0, 12],
         [0, 0, 0, 0, 11, 0, 6],
         [0, 0, 0, 0, 0, 0, 0]]
factories = [(1, 12), (0, 9)]
shops = [(4, 4), (6, 6)]