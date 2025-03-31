# 1) Given 2D array [N][N] in which each cell has the value "W" representing water or "L" representing land.
# Lake is a group of water cells connected by their banks. Count how many lakes are in array and how many cells
# has the biggest lake.

# 2) Assuming that array[0][0] and array[n-1][n-1] are land. Check if it is possible to go from [0][0] to [n-1][n-1]
# by land. You can only walk sideways not diagonally. Also find the shortest path between these cells.
from queue import PriorityQueue
from queue import Queue
inf = float('inf')

def dfs(T, visited, row, col, size):
    if row < 0 or row >= len(T) or col < 0 or col >= len(T) or T[row][col] == "L" or visited[row][col]:
        return size

    size += 1
    visited[row][col] = True
    actual_size = size
    actual_size = dfs(T, visited, row - 1, col, actual_size)
    actual_size = dfs(T, visited, row, col - 1, actual_size)
    actual_size = dfs(T, visited, row, col + 1, actual_size)
    actual_size = dfs(T, visited, row + 1, col, actual_size)
    return actual_size

def lakes(T):
    n = len(T)
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = max_lake = 0
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i][j] == "W" and not visited[i][j]:
                count += 1
                max_lake = max(dfs(T, visited, i, j, 0), max_lake)
    return count, max_lake

def possible_moves(T, row, col, child):
    new_row = [row + 1, row, row - 1, row]
    new_col = [col, col + 1, col, col - 1]
    for i in range(len(new_row)):
        if 0 <= new_row[i] < len(T) and 0 <= new_col[i] < len(T):
            if T[new_row[i]][new_col[i]] == "L" and not child[new_row[i]][new_col[i]]:
                return new_row[i], new_col[i]
            elif child[new_row[i]][new_col[i]] is True:
                continue
            elif child[new_row[i]][new_col[i]] is not False and row == child[new_row[i]][new_col[i]][0] and \
                    col == child[new_row[i]][new_col[i]][1]:
                last_row = new_row[i]
                last_col = new_col[i]
                child[row][col] = True
    return last_row, last_col

def lake_bfs(T, w, k):
    n = len(T)
    queue = Queue()
    child = [[False for _ in range(n)] for _ in range(n)]
    d = [[inf for _ in range(n)] for _ in range(n)]
    d[0][0] = 1
    queue.put((w, k))
    while not queue.empty():
        row, col = queue.get()
        if d[row][col] != inf:
            new_row, new_col = possible_moves(T, row, col, child)
            if not child[new_row][new_col]:
                d[new_row][new_col] = d[row][col] + 1
                child[row][col] = (new_row, new_col)
            if new_row == n - 1 and new_col == n - 1:
                return True, d[n-1][n-1], child
            if new_row == 0 and new_col == 0:
                return False, inf, child
            queue.put((new_row, new_col))

def rec(T, w = 0, k = 0, r = 0):
    n = len(T)
    if w == k == n - 1:
        return 0
    if not (0 <= w < n and k < n) or T[w][k] == "W":
        return -1
    a = b = c = -inf
    if r >= 0:
        a = rec(T, w + 1, k, 1)
    if r <= 0:
        b = rec(T, w - 1, k, -1)
    c = rec(T, w, k + 1, 0)
    return max(a, b, c) + 1

def possibles(G, w, k):
    n = len(G)
    y = [w - 1, w + 1, w]
    x = [k, k, k + 1]
    possibles = []
    for i in range(3):
        if 0 <= y[i] < n and 0 <= x[i] < n and T[y[i]][x[i]] == "L":
            possibles.append((y[i], x[i]))
    return possibles

def dfs_lake(T, w, k):
    n = len(T)
    visited = [[False for _ in range(n)] for _ in range(n)]
    d = [[inf for _ in range(n)] for _ in range(n)]
    parent = [[None for _ in range(n)] for _ in range(n)]

    def DFS_visit(w, k):
        visited[w][k] = True

        vertices = possibles(T, w, k)
        if len(vertices) != 0:
            for y, x in vertices:
                if not visited[y][x] or d[y][x] > d[w][k] + 1:
                    parent[y][x] = (w, k)
                    d[y][x] = d[w][k] + 1
                    DFS_visit(y, x)

    d[w][k] = 0
    DFS_visit(w, k)
    return d

T = [["L", "W", "L", "L", "L", "L", "L", "L"],
     ["L", "W", "L", "W", "W", "L", "L", "L"],
     ["L", "L", "L", "W", "W", "L", "W", "L"],
     ["L", "W", "W", "W", "W", "L", "W", "L"],
     ["L", "L", "W", "W", "L", "L", "L", "L"],
     ["L", "W", "L", "L", "L", "L", "W", "W"],
     ["W", "W", "L", "W", "W", "L", "W", "L"],
     ["L", "L", "L", "W", "L", "L", "L", "L"]]

# print(lakes(T))
# print(*lake_bfs(T, 0, 0)[2], sep='\n')
# print(rec(T, 0, 0, 0))
print(*dfs_lake(T, 0, 0), sep ='\n')