#Sklejanie odcinków
#Dwa odcinki wolno skleić wtedy, gdy ich przecięcie zawiera dokładnie 1 punkt
#a) czy da się uzyskać odcinek [a, b] poprzez sklejanie niektórych odcinków?
#b) = a, ale sklejać wolno najwyżej k odcinków
#c) = b, ale każdy odcinek ma dodatnią cenę i minimalizujemy sumę cen wszystkich odcinków

#d) jaki najdłuższy odcinek można uzyskać sklejając najwyżej k odcinków?

from queue import Queue
from queue import PriorityQueue
inf = float('inf')

def makegraph(T):
    m = len(T)
    n = 0
    for i in range(m):
        n = max(n, T[i][1])
    G = [[] for _ in range(n + 1)]
    for u, v, l in T:
        G[u].append((v, l))
    return G

def BFS(G, s):
    n = len(G)
    visited = [False for _ in range(n)]
    d = [-1 for _ in range(n)]
    q = Queue()
    visited[s] = True
    d[s] = 0
    q.put(s)
    while not q.empty():
        u = q.get()
        for v, l in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                q.put(v)
    return d, visited

def relax(u, v, l, d, e, q, k):
    if d[v] > d[u] + l and e[u] + 1 <= k:
        d[v] = d[u] + l
        e[v] = e[u] + 1
        q.put((e[v], d[v], v))

def Dijkstry(G, s, k):
    n = len(G)
    d = [inf for _ in range(n)]
    e = [inf for _ in range(n)]
    q = PriorityQueue()
    d[s] = 0
    e[s] = 0
    q.put((e[s], d[s], s))
    while not q.empty():
        eu, du, u = q.get()
        if d[u] == du and e[u] == eu:
            for v, l in G[u]:
                relax(u, v, l, d, e, q, k)
    return d

def odcinki(T, A, B, k):
    G = makegraph(T)
    n = len(G)
    d, visited = BFS(G, A)
    a = visited[B]
    b = (d[B] <= k)
    c = Dijkstry(G, A, k)[B]
    return a, b, c

def length(a):
    return a[1] - a[0]

def connect(a, b):
    if length(a) == 0:
        return b
    if length(b) == 0:
        return a
    if a[0] == b[1]:
        return(b[0], a[1])
    if b[0] == a[1]:
        return(a[0], b[1])

    return False

def odcinki_d(T, B):
    n = len(T)
    F = [[0 for _ in range(B + 1)] for _ in range(n)]
    C = [[(0, 0) for _ in range(B + 1)] for _ in range(n)]
    for b in range(1, B + 1):
        F[0][b] = (T[0][1] - T[0][0])
        C[0][b] = T[0]
    for b in range(1, B + 1):
        for i in range(1, n):
            F[i][b] = F[i-1][b]
            C[i][b] = C[i-1][b]

            l = connect(C[i-1][b-1], T[i])
            if l and length(l) > F[i][b]:
                F[i][b] = length(l)
                C[i][b] = l

    # print(*F, sep='\n')
    # print()
    # print(*C, sep='\n')
    print(*C, sep='\n')
    return F[n-1][B]

def my_odcinki_d(T, B):
    n = len(T)
    DP = [[(0, 0) for _ in range(B + 1)] for i in range(n)]
    for b in range(1, B + 1):
        DP[0][b] = T[0]
    for i in range(1, n):
        for b in range(1, B + 1):
            if length(DP[i][b-1]) > length(DP[i-1][b]):
                DP[i][b] = DP[i][b - 1]
            else:
                DP[i][b] = DP[i-1][b]
            for j in range(i):
                p = connect(DP[j][b - 1], T[i])
                if p and length(p) > length(DP[i][b]):
                    DP[i][b] = p
    print(*DP, sep='\n')
    return length(DP[n-1][b])


P = [(0, 1, 2), (1, 3, 4), (2, 5, 9), (3, 4, 10), (5, 8, 1), (4, 8, 7), (8, 11, 5), (11, 15, 8), (11, 12, 2), (12, 16, 3)]
T1 = [(0, 1), (1, 3), (2, 5), (3, 4), (4, 8), (5, 8), (8, 11), (11, 15), (11, 12), (12, 16)]
k = 3
print(odcinki(P, 0, 16, k))
print(my_odcinki_d(T1, k))