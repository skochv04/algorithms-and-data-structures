#Black Forest, tablica n drzew, przechowuje zyski.
#Musimy znalezc maksymalny zysk, scinając drzewa, ale nie można
#ścinać два підряд
def wycinka(T, cache, i):
    if i == 0:
        return T[0]
    if i == 1:
        return max(T[0], T[1])
    cache[i] = max(wycinka(T, cache, i -1), wycinka(T, cache, i - 2) + T[i])
    return cache[i]

def wycinka_iter(T):
    n = len(T)
    cache = [0 for _ in range(n)]
    cache[0] = T[0]
    # cache[1] = max(T[0], T[1])
    for i in range(1, n):
        cache[i] = max(cache[i-1], cache[i-2] + T[i])
    return cache[n-1]


T = [1, 2, 3, 4, 5, 6]
n = len(T)
cache = [-1 for _ in range(n)]
print(wycinka(T, cache, 0))
print(wycinka_iter(T))