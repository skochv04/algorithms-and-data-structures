# We have a layout of dominoes. We have it as a list of pairs [a, b]. If we knock over block a, block
# b will also fall over. Find the minimum number of blocks that need to be knocked over by hand so that
# all dominoes are downed.
def make_graph(edges):
    n = len(edges)
    max_vertex = 0
    for i in range(n):
        max_vertex = max(max_vertex, max(edges[i]))
    G = [[] for _ in range(max_vertex)]
    for i in range(n):
        G[edges[i][0]-1].append(edges[i][1]-1)
    return G

def topsort(G):
    n = len(G)
    visited = [False for _ in range(n)]
    def DFS_visit(G, u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_visit(G, v)
        tab.append(u+1) #topsort

    time = 0
    tab = [] #topsort
    for u in range(len(G)):
        if not visited[u]:
            DFS_visit(G, u)
    return tab[::-1]

def domino(edges, start):
    G = make_graph(edges)
    tab = topsort(G)
    n = len(tab)
    sum = 1
    print(tab)
    for i in range(n-1):
        if i + 1 not in G[i]:
            sum += 1
    return sum

dominos =  [[1, 3], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]
print(domino(dominos, 0))