# The internet cafe has K computers and A applications on CDs. Maximum one application can be installed
# on each computer. Each application has a list of computers on which it can run and the rest cannot, due
# to hardware requirements. We are the owner of a cafe and we know haw many customers (possibly zero) will
# would like to use the application tomorrow. We assume that each client occupies a computer for the
# whole day. What an application should we install on each of the computers so that all customers can use
# the application which they want. If there is not such an assignment, the algorithm should consider that.

from queue import Queue

def find_path(G, s, t):
    n = len(G)
    q = Queue()
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    visited[s] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.put(v)
    tab = None
    if parent[t] != None:
        ind = t
        tab = []
        while ind != parent[s]:
            tab.append(ind)
            ind = parent[ind]
        tab = tab[::-1]
    return tab

def ford_fulkerson(G, s, t):
    n = len(G)
    count = 0
    my_path = find_path(G, s, t)
    tab = []
    while my_path:
        count += 1
        tab.append((my_path[1], my_path[2]))
        for i in range(len(my_path) - 1):
            G[my_path[i]].remove(my_path[i+1])
            G[my_path[i+1]].append(my_path[i])
        my_path = find_path(G, s, t)
    return count, tab

def internet_cafe(G, computers, applications, demand_applications):
    n = len(G)
    c = len(computers)
    for i in range(n, n+c):
        G.append([n+c+1])
    G.append([])
    clients = 0
    for i in range(n):
        for q in range(demand_applications[i]):
            clients += 1
            G[n+c].append(i)
    G.append([])
    n = len(G)
    result = ford_fulkerson(G, n-2, n-1)
    if result[0] != clients:
        return None
    return result[1]

def my_internet_cafe(G, computers, applications, demand_applications):
    n = len(applications)
    c = len(computers)
    for i in range(n, n + c):
        G.append([n+c+1])
    G.append([])
    for i in range(n):
        G[n+c].append(demand_applications[i])
    G.append([])
    n = len(G)
    result = ford_fulkerson(G, n-2, n-1)
    if result[0] != len(demand_applications):
        return False
    return result


applications = [0, 1, 2, 3]
computers = [4, 5, 6, 7, 8]

demand_applications = [2, 2, 0, 1]
G = [[4, 7], [5, 6, 7], [7, 8], [8]]
print(my_internet_cafe(G, computers, applications, demand_applications))
