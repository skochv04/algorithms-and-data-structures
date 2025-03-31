#Stas Kochevenko
#Opis: W danym algorytmie skorzystamy się z funkcji f(i, b), która oznacza minimalny koszt znalezienia się na planecie i
#mając b ton paliwa.
#f(0, 0) = 0 (nie potrzebujemy paliwa żeby dostać się do 0 planety)
#f(0, b) = nieskończonność (nie jesteśmy w stanie mieć b paliwa, nie podróżując).
#Dla każdej planety k, która znajduje się przed i, próbujemy dotrzeć z niej do i teleportem, jeśli mamy 0 paliwa (jeśli
#skorzystamy z tego, to będziemy mieli 0 paliwa). Następnie dla każdej potencjalnej ilości paliwa od 0 do pojemności baku
#wyznaczamy minimum pomiędzy aktualnej wartością funkcji i, lotem z planety k, mając 0 paliwa (kupujemy niezbędne do
#dotarcia paliwo na planecie k) oraz łądowaniem na planecie k, mając wystarczającą ilość paliwa do dotarcia do planety i.
#W wyniku działania algorytmu zwrócamy minimum z f(n-1, k[od 0 do E+1]). Złożoność to O(n^2E).

from egz1btesty import runtests
inf = float('inf')

def planets( D, C, T, E ):
    n = len(D)
    dp = [[inf for _ in range(E + 1)] for _ in range(n)]
    dp[0][0] = 0
    for i in range(1, n):
        for k in range(i):
            if T[k][0] == i and T[k][0] != k:
                dp[i][0] = min(dp[i][0], dp[k][0] + T[k][1])
            for j in range(E + 1):
                if j + D[i] - D[k] < E + 1:
                    dp[i][j] = min(dp[i][j], dp[k][j + D[i] - D[k]], dp[k][0] + C[k] * (j + D[i] - D[k]))
    return min(dp[n-1])

D = [ 0, 5, 10, 20]
C = [ 2, 1, 3, 9]
T = [(2,3), (3,7), (2,10), (3,10)]
E = 10
print(planets(D, C, T, E))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
