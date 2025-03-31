#8) formuły logiczne (określić wartościowanie -> wart poszczególnych zmiennych - normalnie problem NP trudny)
#   -> postać normalna koniunkcyjna, każda zmienna występuje dokładnie dwa razy (raz z negacją, raz be) -> krawędź
#   skierowana w grafie to implikacja (mamy więcej zmiennych niż alternatyw), skojarzenie maksymalne pomiędzy
#   A={a,~a,...} B=((a v b),(b v ~c),...) -> bierzemy te krawędzie, które są w maksymalnym skojarzeniu
#   lub: b) wierzchołkami klauzule, wagi - zmienne bez negacji, trzeba nadać skierowanie tak, by na każdy wierzchołek
#   wskazywała przynajmniej jedna krawędź, jeśli mamy drzewo, to nie da się znaleźć takiego wartościowania, jeśli cykl,
#   to łączymy w kółko, zamieniamy cykl w wierzchołek i uruchamiamy DFS

from copy import deepcopy


from collections import deque

def find_path(G, s, t):
    #BFS/DFS
    n = len(G)
    visited = [False for _ in range(n)]
    d = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = deque()
    d[s] = 0
    visited[s] = True
    Q.append(s)
    while len(Q):
        u = Q.popleft()
        for v in range(n):
            if G[u][v] and not visited[v]:
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
                Q.append(v)
    tab = None
    if parent[t] != None:
        ind = t
        tab = []
        while ind != parent[s]:
            tab.append(ind)
            ind = parent[ind]
        tab = tab[::-1]
    return tab


def min_weight(G, path):
    #Проходимо по всьому шляху і шукаємо мінімальну вагу на ньому
    w = G[path[0]][path[1]]
    for i in range(1, len(path) - 1):
        w = min(w, G[path[i]][path[i + 1]])
    return w

def update_weights(G, path, w):
    for i in range(len(path)-1):
        G[path[i]][path[i+1]] -= w
        G[path[i+1]][path[i]] += w


def construct_graph(formula):
    variables = []
    clauses = formula.split(" ^ ")
    for clause in clauses:
        literals = clause.split(" v ")
        for literal in literals:
            if literal[0] == "~":
                var = literal[1:]
                if var not in variables:
                    variables.append(var)
            else:
                var = literal
                if var not in variables:
                    variables.append(var)
    n = len(variables)
    graph = [[0 for _ in range(2 * n + 2)] for _ in range(2 * n + 2)]
    for i in range(1, n + 1):
        graph[0][i] = 1
        graph[i][i + n] = 1
    for i in range(n + 1, 2 * n + 1):
        graph[i][2 * n + 1] = 1
    for clause in clauses:
        literals = clause.split(" v ")
        u, v = 0, 0
        for literal in literals:
            if literal[0] == "~":
                u = variables.index(literal[1:]) + 1
            else:
                v = variables.index(literal) + n + 1
        graph[u][v] = 1
    return graph

def ford_fulkerson(G, s, t):
    n = len(G)
    count = 0
    my_path = find_path(G, s, t)
    while my_path:
        w = min_weight(G, my_path)
        count += w
        update_weights(G, my_path, w)
        my_path = find_path(G, s, t)
    return count

formula = "(a v ~b) ^ (b v ~c) ^ (c v a)"
G = construct_graph(formula)
print(ford_fulkerson(G, 0, 2 * len(G) - 1))