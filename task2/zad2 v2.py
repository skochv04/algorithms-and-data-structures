#Stas Kochevenko
#Opis: Najpierw sortujemy elementy za pomocą alorytmu count_sort, potem ustalamy zmienną długości tablicy i zmienną
#mniejszą od długości o 1, jako iterator. Ustalamy zmienną sumy = 0, a następnie w pętli będziemy dodawać do niej
#wartość ostatniego (maksymalnego) elementu tablicy zmniejszonego o różnicy pomiędzy długością tablicy a indexem
#danego elementu minus 1. W każdej kolejniej iteracji zmniejszamy zmienną-iterator, dopóki nie wyjdziemy poza tablicę,
#albo wartość elementu o indexie itaratora będzie mniejsza od różnicy pomiędzy długością tablicy a indexem danego
#elementu minus 1. Złożoność obliczeniowa wynosi O(n+k).

from zad2testy import runtests

# def findmax(T):
#     n = len (T)
#     max_el = 0
#     for i in range (n):
#         if T[i] > max_el:
#             max_el = T[i]
#     return max_el
#
# def count_sort(T):
#     n = len(T)
#     c = [0 for _ in range(findmax(T) + 1)]
#     output = [0 for _ in range(n)]
#     for i in range(n):
#         c[T[i]] += 1
#     for i in range(1, len(c)):
#         c[i] += c[i - 1]
#     for i in range(n):
#         c[T[i]] -= 1
#         output[c[T[i]]] = T[i]
#     for i in range(n):
#         T[i] = output[i]
#     return T
#
# def snow( S ):
#     count_sort(S)
#     n = len(S)
#     i = n - 1
#     sum = 0
#     while i > -1 and S[i] > n - i - 1:
#         sum += S[i] - (n - i - 1)
#         i -= 1
#     return sum

# zmien all_tests na True zeby uruchomic wszystkie testy

def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    return (i - 1) // 2


# Jak na wykladzie
def heapify(tab, i, n):
    l = left(i)
    r = right(i)
    max_idx = i
    if l < n and tab[l] > tab[max_idx]:
        max_idx = l
    if r < n and tab[r] > tab[max_idx]:
        max_idx = r
    if max_idx != i:
        tab[i], tab[max_idx] = tab[max_idx], tab[i]
        heapify(tab, max_idx, n)


def build_heap(tab):
    n = len(tab)
    for i in range(parent(n-1), -1, -1):
        heapify(tab, i, n)


# def snow( S ):
#     # tu prosze wpisac wlasna implementacje
#     n = len(S)
#     collected = 0
#     build_heap(S)
#     days = 0
#     for i in range(n-1, 0, -1):
#         S[0], S[i] = S[i], S[0]
#         if S[i] > days:
#             collected += S[i] - days
#             days += 1
#         else:
#             return collected
#         heapify(S, 0, i)

def snow( S ):
    build_heap(S)
    n = len(S)
    sum = 0
    i = n - 1

    for i in range(n-1, 0, -1):
        S[0], S[i] = S[i], S[0]
        if S[i] > n - i - 1:
            sum += S[i] - (n - i - 1)
        else:
            return sum
        heapify(S, 0, i)

    return sum


T = [1, 7, 3, 4, 1]
print (snow (T))
runtests( snow, all_tests = True )