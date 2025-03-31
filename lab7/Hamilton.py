def is_hamiltonian(G, path=None, visited=None):
    n = len(G)
    if path is None:
        path = []
    if visited is None:
        visited = [False for _ in range(n)]
    if len(path) == n:
        # Перевіряємо, чи існує ребро між першою і останньою вершиною
        if G[path[0]][path[-1]]:
            return True
        return False
    for v in range(n):
        if not visited[v]:
            if not path or G[path[-1]][v]:
                path.append(v)
                visited[v] = True
                if is_hamiltonian(G, path, visited):
                    return True
                path.pop()
                visited[v] = False
    return False


# G = [[0, 1, 1, 0, 0, 0, 0],
#      [0, 0, 1, 1, 1, 1, 1],
#      [0, 1, 0, 1, 1, 1, 1],
#      [0, 1, 1, 0, 1, 1, 0],
#      [0, 1, 1, 1, 0, 1, 0],
#      [0, 1, 1, 1, 1, 0, 0],
#      [0, 1, 1, 0, 0, 0, 0]]

G = [[0, 1, 1, 0, 1],
     [1, 0, 1, 0, 1],
     [1, 1, 0, 1, 0],
     [0, 0, 1, 0, 1],
     [1, 1, 0, 1, 0]]

print(is_hamiltonian(G))