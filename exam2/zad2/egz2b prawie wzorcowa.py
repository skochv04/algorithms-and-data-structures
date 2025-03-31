#Stas Kochevenko
#Opis: W danym algorytmie korzystam z funkcji, zaproponowanej w podpowiedzi. Dla każdego X[i] biurowca zakładam,
#że przydzielona mu działka to Y[j], a wszystkie biórowcy na pozycjach do i już mają przydzieloną działke. Oprócz tego,
#mam dodatkową tablicę, w której przechowywam minimalną odległość, którą udało się osiągnąć dla poprzedniego biórowcy
#spośród j działek. Dzięki temu optymalizuję złożoność czasową. Więc, sprawdzam możliwości przydzielenia, minimalizując
#odległość pomiędzy biórowcem i działką, oraz nie rozważam działek na pozycjach mniejszych od przydzielonej działki
#biórowcu X[i-1]. Za każdym razem zmieniam danę w pomocnieczej tablicy w taki sposób, żeby ona przechowywała informację
#o każdym następnym rozważanym biurówce. Algorytm ma złożoność O(nm).

from egz2btesty import runtests
inf = float('inf')

def dist(a, b):
  return abs(a - b)

def parking(X,Y):
  n = len(X)
  m = len(Y)
  DP = [[inf for _ in range(m)] for _ in range(n)]
  T = [inf for _ in range(m + 1)]
  for j in range(m):
    d = dist(X[0], Y[j])
    DP[0][j] = d
    T[j + 1] = min(T[j], d)
  for i in range(1, n):
    prev = T[i]
    T[i] = T[i-1]
    for j in range(i, m):
      loc_dist = dist(X[i], Y[j])
      DP[i][j] = loc_dist + prev
      prev = T[j+1]
      T[j+1] = min(T[j], DP[i][j])
  min_dist = DP[n-1][0]
  for j in range(m):
    min_dist = min(min_dist, DP[n-1][j])
  return min_dist

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
