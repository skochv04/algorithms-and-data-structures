#Stas Kochevenko
#Opis: W danym algorytmie korzystam z funkcji, zaproponowanej w podpowiedzi. Dla każdego X[i] biurowca zakładam,
#że przydzielona mu działka to Y[j], a wszystkie biurowcy na pozycjach do i już mają przydzieloną działke, przy
#założeniu, że współrzędna j-ej działki większa od współrzędnej przyznaczonej i-1 elementowi działki. Obliczam warunki
#brzegowe (odległość od pierwszego biurowca do każdej możliwej działki), a następnie dla każdego i+1-ego biurowcy ustalam
#minimalną odległość jako odległość do j-ej działki plus minimalna odległość, którą udało się osiągnąć dla i-tego biurowcy,
#rozważając działki od 0 do j-1. Dzięki temu optymalizuję złożoność algorytmu, która wynosi O(nm).

from egz2btesty import runtests
inf = float('inf')

def dist(a, b):
  return abs(a - b)

def parking(X,Y):
  n = len(X)
  m = len(Y)
  DP = [[inf for _ in range(m)] for _ in range(n)]
  for j in range(m):
    DP[0][j] = dist(X[0], Y[j])
  for i in range(n-1):
    loc_min = inf
    for j in range(m):
      loc_dist = dist(X[i+1], Y[j])
      DP[i+1][j] = loc_dist + loc_min
      loc_min = min(loc_min, DP[i][j])

  min_dist = DP[n-1][0]
  for j in range(m):
    min_dist = min(min_dist, DP[n-1][j])
  return min_dist

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
