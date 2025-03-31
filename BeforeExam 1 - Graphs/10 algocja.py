# Algocia is placed on a great dessert and consists of cities and oases connected by roads. There is
# exactly one road leading from each gate to one oasis (but any given oasis can have any number of roads
# leading to them, oases can also be interconnected by roads). Algocian law requires that if someone
# enters a city through one gate, they must leave the other. Check of Algocia decided to send a bishop
# who will read the prohibition of formulating tasks "about the chessboard" (insult majesty) task in
# every city. Check wants the bishop to visit each city exactly once (but there is no limit how many
# times the bishop will visit each oasis). Bishop departs from the capital of Algocia city x, and after
# visiting all cities the bishop has to come back to city x. Find algorithm that determines if there
# is a suitable route for bishop.

def create_graph(G, C):
    n = len(G)
    M = [[False, G[i]] for i in range(n)]
    for city in C:
        M[city][0] = True
    return M

def cities_to_edges(G):
    n = len(G)
    new_oasis_indices = [-1] * n

    idx = 0
    for i in range(n):
        if not G[i][0]:
            new_oasis_indices[i] = idx
            idx += 1

    # Create a new graph
    new_n = idx
    new_G = [[0, []] for _ in range(new_n)]
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            if G[i][0]:
                u = G[i][1][0]
                v = G[i][1][1]
                # While at least one of the neighbours is a city, loop till we reach an oasis
                prev_u = prev_v = i
                while G[u][0]:
                    visited[u] = True
                    u, prev_u = G[u][1][0] if G[u][1][0] != prev_u else G[u][1][1], u
                while G[v][0]:
                    visited[v] = True
                    v, prev_v = G[v][1][0] if G[v][1][0] != prev_v else G[v][1][1], v
                # When both vertices are now oasis, we can add an edge representing
                # all the cities on a way (we have to visit them all at once)
                new_u = new_oasis_indices[u]
                new_v = new_oasis_indices[v]
                new_G[new_u][1].append((True, new_v))  # True means this edge is a city
                new_G[new_v][1].append((True, new_u))  # True means this edge is a city
                # Increment a number of connected city edges (edges which are cities) to the oasis
                new_G[new_u][0] += 1
                new_G[new_v][0] += 1
                # If it's an oasis
            else:
                # An oasis can have multiple neighbours but cities will be covered in the case above,
                # so we will add only edges between oasis in here
                new_u = new_oasis_indices[i]
                for v in G[i][1]:
                    if not G[v][0]:  # If is also an oasis
                        new_v = new_oasis_indices[v]
                        # Add only one edge as the remaining ones will be added from the other oasis
                        new_G[new_u][1].append((False, new_v))  # False means this edge connects two oasis
    return new_G

def degree_after_oasis_merge(G, oasis_u, visited):
    deg = 0

    def dfs(u):
        visited[u] = True
        # If u is a vertex which has at least one city edge connected, all the city
        # edges will be linked to the beginning vertex, so its degree will be increased
        # by the number of city edges outgoing from the u edge
        if G[u][0]:
            nonlocal deg
            deg += G[u][0]

        for i in range(len(G[u][1])):
            # If hasn't been visited yet and is not a city edge
            v = G[u][1][i][1]
            is_city_edge = G[u][1][i][0]
            if not visited[v] and not is_city_edge:
                dfs(v)
    dfs(oasis_u)
    return deg

def does_path_exist(G, C):
    G = create_graph(G, C)
    if len(C) == len(G): return True
    G = cities_to_edges(G)
    n = len(G)
    visited = [False] * n
    print(*G, sep='\n')
    for u in range(n):
        if not visited[u]:
            deg = degree_after_oasis_merge(G, u, visited)
            print(u, deg)
            if deg % 2:
                return False
    return True


graph = [[2, 4], [2, 9], [0, 1, 4, 3], [2, 5], [0, 2, 6, 9], [3, 7, 8], [4, 7], [5, 6, 8], [5, 7], [1, 4]]
cities = [0, 1, 3, 6, 8]
print(does_path_exist(graph, cities))