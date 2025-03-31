#Stas Kochevenko
#Rozwiązanie polega na tym, że najpierw sortujemy tablicę z punktami po współrzędnej y, a następnie dla każdego punktu
#z tablicy P, spośród punktów, współrzędna y których mniejsza od aktualnie rozważanego punktu, znajdujemy maksymalną
#liczbę punktów, nad którymi dominuje rozważany punkt. W wyniku działania algorytmu zwrócamy maksymalną silę spośród
#sił każdego punktu. Złożoność algorytmu to O(nlogn).

from egz2atesty import runtests

def dominance(P):
  n = len(P)
  Y = sorted(P, key=lambda x:x[1])
  X = sorted(P, key=lambda x:x[0])

  x = y = n - 1
  while x > 1 and X[x][0] == X[x-1][0]:
      x -= 1
  while y > 1 and Y[y][0] == Y[y-1][0]:
      y -= 1
  while y > 0 and X[x] != Y[y]:
      y -= 1

  res = min(x, y)

  x = y = n - 1
  while x > 0 and X[x] != Y[y]:
      x -= 1
  res = max(res, min(x, y))
  return res
P = [(2, 7), (6, 7), (6, 3), (10, 9), (2, 3), (10, 5), (10, 1), (4, 3), (10, 7), (4, 7)]
#6
print(dominance(P))
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
