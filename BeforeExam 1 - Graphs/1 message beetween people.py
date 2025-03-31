# Given list of people who know each other. People are represented as number between 0 and n-1.
# First day person 0 passes the message to all his friends. Second day each friend passes this
# message to all their friends who doesn't know this message and so on. Find algorithm that
# returns the day when the most people knew the message and the number of people who received it
# that day.

from collections import deque

def message(G, s):
    n = len(G)
    q = deque()
    d = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    d[s] = 1
    visited[s] = True
    q.append(s)
    while len(q) != 0:
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                q.append(v)
    c = max(d)
    sum = 0
    for i in range(n):
        if d[i] == c:
            sum += 1
    return max(d), sum

G = [[1, 2],
     [0, 3, 4],
     [0, 5, 6],
     [1, 10],
     [1, 5, 7, 8, 7, 9, 11],
     [2, 4, 6],
     [2, 5],
     [4],
     [4],
     [4],
     [3],
     [4]]
print(message(G, 0))