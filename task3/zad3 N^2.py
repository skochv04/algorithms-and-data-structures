#Stas Kochevenko
#Opis:

from zad3testy import runtests

def rownowazne(a, b):
    A = len(a)
    B = len(b)
    if A != B:
        return False
    res = True
    for i in range(A):
        if a[i] != b[i]:
            res = False
    if res == True:
      return res
    res = True
    for i in range(A):
        if a[i] != b[B - 1 - i]:
            res = False
    return res

def strong_string(T):
    n = len(T)
    s = 1
    for i in range(n):
        loc_s = 0
        for j in range(n):
            if rownowazne(T[i], T[j]):
                loc_s += 1
        if loc_s > s:
            s = loc_s
    return s


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
