#Stas Kochevenko
#Rozwiązanie polega na tym, że najpierw sortujemy tablicę z punktami po współrzędnej y, a następnie dla każdego punktu
#z tablicy P, spośród punktów, współrzędna y których mniejsza od aktualnie rozważanego punktu, znajdujemy maksymalną
#liczbę punktów, nad którymi dominuje rozważany punkt. W wyniku działania algorytmu zwrócamy maksymalną silę spośród
#sił każdego punktu. Złożoność algorytmu to O(nlogn).

from egz2atesty import runtests

def dominance(P):
  n = len(P)
  sila = 0
  P.sort(key=lambda x: x[1])
  for i in range(n-1, -1, -1):
    loc_sila = 0
    for j in range(i):
      if P[j][0] < P[i][0] and P[j][1] != P[i][1]:
        loc_sila += 1
    sila = max(sila, loc_sila)
  return sila

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
