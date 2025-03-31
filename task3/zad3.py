#Stas Kochevenko
#Opis: Najpierw stworzymy tablicę zer o rozmiarze równym rozmiaru tablicy wejściowej, a następnie w pętli dla każdego
#indeksu od początku do końca tablicy będziemy wpisywali pod zmienną d napis z tablicy (jeżeli kod pierwszej
#litery napisu jest większy od kodu ostatniej litery, to zapiszemy od tyłu), a do stworzonej tablicy zer zamiast
#elementu o danym indeksie będziemy wpisywali krotkę skladającą się z kodu pierwszej litery napisu d, kodu ostatniej
#litery, napisu d oraz jego długości. Po wykonaniu pętli sortujemy RadixSortem tę tablicę za ostatnim indeksem krotki,
#dalej sortujemy liniowo tablicę za 2 indeksem krotki, i w końcu RadixSortem za 2 i 1 indeksami krotek. Po wykonaniu
#tego w kolejnej pętli będziemy porównywać elementy krotki o indeksie 2 (napisy), szujając maksymalnej "siły".

from zad3testy import runtests

def counting_sort(A, ind, place):
    n = len(A)
    C = [0] * 10
    B = [0] * n
    for i in range(n):
        index = A[i][ind] // place
        C[index % 10] += 1
    for i in range(1, 10):
        C[i] = C[i] + C[i-1]
    for i in range(n-1, -1, -1):
        index = A[i][ind] // place
        B[C[index%10]-1] = A[i]
        C[index%10]-=1
    for i in range(n):
        A[i] = B[i]
    return B

def radixSort(A, ind):
    max_element = 122 #kod litery "z", czyli ostatniej w alphabecie
    place = 1
    while max_element // place > 0:
        counting_sort(A, ind, place)
        place *= 10

def strong_string(T):
    n = len(T)
    Tab = [0] * n
    for i in range(n):
        d = min(T[i], T[i][::-1])
        Tab[i] = (ord(d[0]), ord(d[-1]), d, len(d))
    radixSort(Tab, 3)
    # for a in range(1, n):
    #     if Tab[a][2] > Tab[a-1][2]:
    #         Tab[a], Tab[a-1] = Tab[a-1], Tab[a]
    radixSort(Tab, 1)
    radixSort(Tab, 0)

    s = 1
    loc_s = 1
    for p in range(1, n):
        q = p - 1
        if Tab[p][2] == Tab[q][2]:
            loc_s += 1
        else:
            s = max(loc_s, s)
            loc_s = 1
    return s

T = ["pies", "mysz", "kot", "kogut", "kok", "tok", "seip", "kot"]
print(strong_string(T))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
