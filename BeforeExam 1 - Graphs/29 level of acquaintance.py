# We define the relationship of acquaintances as symmetrical.
# Acquaintance:
#   - the first level is the direct acquaintance of the person,
#   - the second level is being a "friend of a friend" of the person, but not being directly acquaintance
# the person,
#   - third level, fourth level, fifth level, etc.,
#   - infinite level is when there is no chain of acquaintance between two people.
# Given a list of people and first level acquaintance between them, find the highest level of acquaintance
# between each of the possible pairs.
from queue import Queue
inf = float('inf')

def BFS(graph, source):
    queue = Queue()
    queue.put(source)
    visited = [False] * len(graph)
    visited[source] = True
    distance = [inf] * len(graph)
    distance[source] = 0
    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if not visited[v]:
                queue.put(v)
                distance[v] = distance[u] + 1
                visited[v] = True
    return distance

def level_of_acquaintance_sparse(people,acquaintance):
    n = len(people)
    d = []
    for i in range(n):
        d.append(BFS(acquaintance, i))
    return d

def level_of_acquaintance_dense(people, acquaintance):
    n = len(people)
    distance = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                distance[i][j] = 0
            elif people[i] in acquaintance[j]:
                distance[people[i]][j] = 1
    for k in range(n):
        for u in range(n):
            for v in range(n):
                distance[u][v] = min(distance[u][v], distance[u][k] + distance[k][v])
    return distance


people = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
acquaintance = [[1, 2, 3], [0, 2, 4, 5], [0, 1, 5, 6], [0, 6], [1, 7], [1, 2, 7], [2, 3, 8],
                [4, 5, 9], [6, 9], [7, 8, 10], [9]]
print(*level_of_acquaintance_sparse(people, acquaintance), sep='\n')
#print(*level_of_acquaintance_dense(people, acquaintance), sep='\n')