#Implementacja zbiorów rozłącznych
class Node:
    def __init__(self, value):
        self.parent = self
        self.rank = 0
        self.value = value

def findset(x):
    if x.parent != x:
        x.parent = findset(x.parent)
    return x.parent

def findset_tab(ind, parent):
    if(parent[ind]) == ind:
        return parent[ind]
    x = findset_tab(parent[ind], parent)
    parent[ind] = x
    return x

def union_tab(tab, x, y):
    n = len(tab)
    # parent = [None for _ in range(n)] ##??
    rank = [0 for _ in range(n)] ##??
    rep_x = findset_tab(x, parent)
    rep_y = findset(y, parent)
    r_x, r_y = rank[rep_x], rank[rep_y]
    if(r_x > r_y):
        parent[r_y] = r_x
    else:
        parent[r_x] = r_y
        if rank[r_x] == rank[r_y]:
            rank[r_x] += 1

T = [0, 1, 2, 3, 4, 5]
#G = [(0,2), (3, 4), (5, 5)] połączone między sobą
parent = [1, 1, 1, 3, 3, 5]