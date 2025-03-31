# After a terrifying forest fire in Berland a forest rebirth program was carried out. Due to it N rows
# with M trees each were planted and the rows were so neat that one could map it on a system of
# coordinates so that the j-th tree in the i-th row would have the coordinates of (i, j). However
# a terrible thing happened and the young forest caught fire. Now we must find the coordinates of the
# tree that will catch fire last to plan evacuation. The burning began in K points simultaneously,
# which means that initially K trees started to burn. Every minute the fire gets from the burning
# trees to the ones that aren’t burning and that the distance from them to the nearest burning tree
# equals to 1. Find the tree that will be the last to start burning. If there are several such trees,
# output any.

#Взагалі треба вивести це дерево, але я зробив тільки карту загоряння, вивести вже не так важко

from queue import Queue

def possible(i, j, N, M):
    x = [j-1, j, j+1, j]
    y = [i, i+1, i, i-1]
    tab = [None for _ in range(4)]
    for k in range(4):
        if 0 <= x[k] < M and 0 <= y[k] < N:
            tab[k] = ((y[k], x[k]))
    return tab

def fire_again(N, M, T):
    visited = [[False for _ in range(M)] for _ in range(N)]
    d = [[-1 for _ in range(M)] for _ in range(N)]
    q = Queue()
    for u, v in T:
        visited[u][v] = True
        q.put((u, v))
        d[u][v] = 0
    while not q.empty():
        u, v = q.get()
        for tree in possible(u, v, N, M):
            if tree != None:
                i, j = tree
                if not visited[i][j]:
                    visited[i][j] = True
                    d[i][j] = d[u][v] + 1
                    q.put((i, j))
    return d

N = 10
M = 10
T = [(1, 3), (7, 9), (8, 1)]
print(*fire_again(N, M, T), sep='\n')