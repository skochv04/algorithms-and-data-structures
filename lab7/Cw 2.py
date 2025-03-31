#Wierzchołek v w grafie skierowanym nazywamy tak zwanym dobrym początkiem, jeżeli każdy inny wieszchołek można
#osiągnąć ścieżką skierowaną wychodzącą z v. Podać algorytm, który dla podanego grafu stwierdza czy G posiada dobry
#początek; lista sąsiedztwa

#Dobre początki - знайти, чи є такі вершини, звідки можна пройти увесь граф, і взагалі їх знайти
#Nie wiemy, czy mamy cykle (nie sortowanie topologiczne)

def check_first(G):
    n = len(G)
    visited = [False for _ in range(n)]

    def DFS_visit(G, u):
        visited[u] = True
        for v in range(n):
            if G[u][v] and not visited[v]:
                DFS_visit(G, v)

    result = DFS_first(G)
    DFS_visit(G, result)
    for x in visited:
        if not x:
            return False
    return result


def DFS_first (G):
    #reprezentacja macierzowa
    n = len(G)
    visited = [False for _ in range(n)]

    def DFS_visit(G, u):
        visited[u] = True
        for v in range(n):
            if G[u][v] and not visited[v]:
                DFS_visit(G, v)
    last = 0
    for ver in range(n):
        if not visited[ver]:
            last = ver
            DFS_visit(G, ver)
    return last

G = [[0, 1, 0, 0, 0],
     [0, 0, 1, 0, 1],
     [0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [0, 0, 1, 0, 0]]

G1 = [[0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0, 0],
      [1, 1, 0, 0, 1, 0, 1],
      [0, 0, 0, 0, 0, 0, 0]]

print(check_first(G1))