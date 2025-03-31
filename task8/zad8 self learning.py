from zad8testy import runtests
from queue import Queue
inf = float('inf')

def find_neighbours(G, u, n, m):
    w, k = u
    x = [k+1, k, k, k-1]
    y = [w, w+1, w-1, w]
    tab = []
    for i in range(4):
        if 0 <= x[i] < m and 0 <= y[i] < n and G[y[i]][x[i]]:
            tab.append((y[i], x[i]))
    return tab


def BFS(G, s):
    n = len(G)
    m = len(G[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = Queue()
    visited[s[0]][s[1]] = True
    if G[s[0]][s[1]]:
        q.put(s)
    suma = G[s[0]][s[1]]
    while not q.empty():
        u = q.get()
        neighbours = find_neighbours(G, u, n, m)
        for v in neighbours:
            if not visited[v[0]][v[1]] and G[v[0]][v[1]]:
                visited[v[0]][v[1]] = True
                suma += G[v[0]][v[1]]
                q.put(v)
    return suma

def my_zaba(T):
    n = len(T)
    energy = sum(T) + 1
    dp = [[(inf, 0) for _ in range(energy + 1)] for _ in range(n)]
    dp[0][T[0]] = (0, 1)
    for i in range(1, n):
        for j in range(energy):
            if dp[i-1][j+1][0] < dp[i][j][0]:
                dp[i][j] = (dp[i-1][j+1][0] + dp[i-1][j+1][1], 0)
                if dp[i][j][0] < dp[i][j + T[i]][0]:
                    dp[i][j + T[i]] = (dp[i][j][0], 1)
    return min(dp[-1])[0]

def falisz_zaba(T):
    n = len(T)
    energy = sum(T) + 1
    dp = [[inf for _ in range(energy + 1)] for _ in range(n)]
    dp[0][T[0]] = 0
    for i in range(n):
        for j in range(i):
            for a in range(energy):
                if 0 <= a + (i - j) - T[j] < energy:
                    dp[i][a] = min(dp[i][a], dp[j][a + (i - j) - T[j]] + 1)
    print(*dp, sep='\n')
    return min(dp[-1])

def my_greedy_zaba(F):
    m = len(F)
    tab = [(F[i], i) for i in range(m)]
    tab.sort(key=lambda x: x[0])
    tab = tab[::-1]
    visited = [False for _ in range(m)]
    jumps = 1
    dist = F[0]
    i = 0
    visited[i] = True
    while dist < m-1 and i < m:
        energy, place = tab[i]
        if 0 < place <= dist and not visited[i]:
            dist += energy
            jumps += 1
            visited[i] = True
            i = 0
        i += 1
    return jumps

def plan(T):
    m = len(T[0])
    F = [BFS(T, (0, i)) for i in range(m)]
    print(F)
    return my_zaba(F)




T = [[3, 0, 0, 1, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [4, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


print(plan(T))
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )