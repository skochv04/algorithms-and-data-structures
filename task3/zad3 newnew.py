from zad3testy import runtests

def find_max(T):
    maxi = 1
    for word, l in T:
        maxi = max(maxi, l)
    return maxi

def counting_sort(A, k, ind):
    n = len(A)
    C = [0] * k
    B = [0] * n
    for i in range(n):
        C[A[i][ind]] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    for i in range(n-1, -1, -1): #zachowujemy stabilność!!!
        B[C[A[i][ind]]-1] = A[i]
        C[A[i][ind]]-=1
    for i in range(n):
        A[i] = B[i]
    return B

def counting_sort_aplha(A, place):
    n = len(A)
    a = 97
    b = 122
    k = b-a+1
    C = [0] * k
    B = [0] * n
    for i in range(n):
        C[ord(A[i][place])-a] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1): #zachowujemy stabilność!!!
        C[ord(A[i][place])-a]-=1
        B[C[ord(A[i][place])-a]] = A[i]
    return B

def radixSort(A):
    for place in range(len(A[0]) - 1, -1, -1):
        A = counting_sort_aplha(A, place)
    return A

def strong_string(T):
    n = len(T)
    for i in range(n):
        if ord(T[i][0]) > ord(T[i][-1]):
            T[i] = (T[i][::-1], len(T[i]))
        else:
            T[i] = (T[i], len(T[i]))
    k = find_max(T)

    buckets = [[] for _ in range(k + 1)]
    for i in range(len(T)):
        buckets[T[i][1]].append(T[i][0])
    for i in range(len(buckets)):
        if len(buckets[i]) != 0:
            buckets[i] = radixSort(buckets[i])
    result = []
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            result.append((buckets[i][j], len(buckets[i][j])))
    res = 1
    loc_res = 1
    for i in range(1, n):
        if result[i][1] == result[i-1][1] and result[i][0] == result[i-1][0]:
            loc_res += 1
        else:
            res = max(res, loc_res)
            loc_res = 1
    return res

# T = ["pies", "mysz", "kot", "kogut", "kok", "tok", "seip", "kot"]
# print(strong_string(T))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
