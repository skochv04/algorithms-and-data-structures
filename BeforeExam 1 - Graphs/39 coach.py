# A programming coach has n students to teach. We know that n is divisible by 3. Let's assume that
# all students are numbered from 1 to n, inclusive. Before the university programming championship
# the coach wants to split all students into groups of three. For some pairs of students we know that
# they want to be on the same team. Besides, if the i-th student wants to be on the same team with
# the j-th one, then the j-th student wants to be on the same team with the i-th one. The coach wants
# the teams to show good results, so he wants the following condition to hold: if the i-th student
# wants to be on the same team with the j-th, then the i-th and the j-th students must be on the
# same team. Also, it is obvious that each student must be on exactly one team. Help the coach and
# divide the teams the way he wants.

def coach(n, m, T):
    G = [[] for _ in range(n + 1)]
    for u, v in T:
        G[u].append(v)
        G[v].append(u)
    tab = [[] for _ in range(n//3)]
    actual = 0
    visited = [False for _ in range(n + 1)]
    visited[0] = True
    for u in range(1, n+1):
        if not visited[u] and len(G[u]) == 2:
            visited[u] = True
            tab[actual].append(u)
            for v in G[u]:
                visited[v] = True
                tab[actual].append(v)
            actual += 1
    sec_actual = actual
    for u in range(1, n+1):
        if not visited[u] and len(G[u]) == 1:
            visited[u] = True
            tab[sec_actual].append(u)
            for v in G[u]:
                visited[v] = True
                tab[sec_actual].append(v)
            sec_actual += 1
        elif not visited[u] and len(G[u]) == 0:
            visited[u] = True
            tab[actual].append(u)
            for v in G[u]:
                visited[v] = True
                tab[actual].append(v)
            actual += 1
    return tab

n = 18
m = 12
T = [(1, 10), (2, 4),(3, 15), (3, 18), (4, 8), (5, 6), (9, 13),
     (12, 14), (12, 16), (14, 16), (15, 18)]
print(*coach(n, m, T), sep ='\n')