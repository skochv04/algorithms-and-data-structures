#Stas Kochevenko
#Opis: Najpierw sortujemy elementy za pomocą alorytmu count_sort, potem ustalamy zmienną długości tablicy i zmienną
#mniejszą od długości o 1, jako iterator. Ustalamy zmienną sumy = 0, a następnie w pętli będziemy dodawać do niej
#wartość ostatniego (maksymalnego) elementu tablicy zmniejszonego o różnicy pomiędzy długością tablicy a indexem
#danego elementu minus 1. W każdej kolejniej iteracji zmniejszamy zmienną-iterator, dopóki nie wyjdziemy poza tablicę,
#albo wartość elementu o indexie itaratora będzie mniejsza od różnicy pomiędzy długością tablicy a indexem danego
#elementu minus 1. Złożoność obliczeniowa wynosi O(n+k).

from zad2testy import runtests

def findmax(T):
    n = len (T)
    max_el = 0
    for i in range (n):
        if T[i] > max_el:
            max_el = T[i]
    return max_el

def count_sort(T):
    n = len(T)
    c = [0 for _ in range(findmax(T) + 1)]
    output = [0 for _ in range(n)]
    for i in range(n):
        c[T[i]] += 1
    for i in range(1, len(c)):
        c[i] += c[i - 1]
    for i in range(n):
        c[T[i]] -= 1
        output[c[T[i]]] = T[i]
    for i in range(n):
        T[i] = output[i]
    return T

def snow( S ):
    count_sort(S)
    n = len(S)
    i = n - 1
    sum = 0
    while i > -1 and S[i] > n - i - 1:
        sum += S[i] - (n - i - 1)
        i -= 1
    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )