#Sprawdzić, czy jest ścieżka Hamiltona w grafie zorientowanym bez cykli. (dag)
#Sortyjemy topologicznie i sprawdzamy czy istnieje krawędż pomiędzy kolejnymi dwoma.

#brut force
def is_hamiltonian(G, path=[], visited=None):
    n = len(G)
    if visited is None:
        visited = [False for _ in range(n)]
    if len(path) == n:
        if G[path[0]][path[-1]] or G[path[-1]][path[0]]:
            return path #True
        return False
    for v in range(n):
        if not visited[v]:
            if not path or G[path[-1]][v]:
                path.append(v)
                visited[v] = True
                if is_hamiltonian(G, path, visited):
                    return path #True
                path.pop()
                visited[v] = False
    return False

def find_hamilton(G):
    n = len(G)
    visited = [False for _ in range(n)]

    def DFS_visit(G, u):
        visited[u] = True
        for v in range(n):
            if G[u][v] and not visited[v]:
                DFS_visit(G, v)
        tab.append(u)
    tab = []
    DFS_visit(G, 0)
    for i in range(n - 1):
        if not G[tab[i+1]][tab[i]]:
            return False
    return tab[::-1]

G1 = [[0, 1, 0],
      [0, 0, 1],
      [1, 0, 0]]

G2 = [[0, 1, 1, 0, 0, 0],
      [0, 0, 0, 1, 0, 1],
      [0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 1],
      [0, 1, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0]]

G3 = [[0, 1, 1, 0, 0, 0, 0],
      [0, 0, 1, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0, 0, 1],
      [0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0]]

print(is_hamiltonian(G1))
print(find_hamilton(G1))
print(is_hamiltonian(G2))
print(find_hamilton(G2))
print(is_hamiltonian(G3))
print(find_hamilton(G3))