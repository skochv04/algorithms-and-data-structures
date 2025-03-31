def insert (T, value):
    T.append (value)
    n = len (T) - 1
    while T[parent(n)] < T[n]:
        T[parent(n)], T[n] = T[n], T[parent(n)]
        n = parent(n)