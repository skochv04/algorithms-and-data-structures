# Algocja leży na wielkiej pustyni i skłąda się z miast, oraz oaz połączonymi drogami, każde miasto jest otoczone
# murem i ma tylko 2 bramy, północną i południową. Z każdej bramy prowadzi dokładnie 1 droga do 1 oazy, do danej oazy
# może dochodzić dowolnie wiele dróg i oazy mogą być połączone drogami między sobą. Prawo algocji wymaga, że jeżeli
# ktoś wjechał do miasta 1 bramą to musi wyjechać drugą. Szach Algocji postanowił wysłać gońca, który w każdym mieście
# odczyta dekret, zakazujący tworzenia zadań algorytmicznych związanych z szachami. Szach chce, żeby goniec odwiedził
# każde miasto dokładnie raz. Goniec wyjeżdża ze stolicy algocji - miasta x i ma do niej wrócić.

def Euler(G):
    n = len(G)
    for i in range(n):
        if len(G[i]) % 2 != 0:
            return False
    visited = [False for _ in range(n)]
    visited_edge = [[False for _ in range(n)] for _ in range(n)]
    last = [0 for _ in range(n)]

    def DFS_visit(G, u):
        nonlocal tab
        visited[u] = True
        for i in range(last[u], len(G[u])):
            v = G[u][i]
            if not visited_edge[u][v]:
                visited[u], visited[v] = True, True
                visited_edge[u][v], visited_edge[v][u] = True, True
                last[u] = i
                DFS_visit(G, v)
        tab.append(u)

    tab = []
    DFS_visit(G, 0)
    for i in range(n): #чи всі відвідані
        if not visited[i]:
            return False
    return tab

def find_path(G, s):
     n = len(G)
     odd = []
     for i in range(n):
          if len(G[i]) % 2 != 0:
               odd.append(i)
     if len(odd) == 0:
          return Euler(G)

     return False


G = [[4, 5],
     [5, 7],
     [6, 7],
     [4, 6],
     [0, 3, 5],
     [0, 1, 4],
     [2, 3, 7],
     [1, 2, 6]]

# G1 = [[4, 5],
#      [5, 7],
#      [6, 7],
#      [4, 6],
#      [0, 3, 5, 7],
#      [0, 1, 4, 6],
#      [2, 3, 5, 7],
#      [1, 2, 4, 6]]

print(find_path(G, 0))