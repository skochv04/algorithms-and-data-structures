#Stas Kochevenko
#Opis: W danym algorytmie korzystam z funkcji, zaproponowanej w podpowiedzi. Dla każdego X[i] biurowca zakładam,
#że przydzielona mu działka to Y[j], a wszystkie biórowcy na pozycjach do i już mają przydzieloną działke. Więc,
#sprawdzam możliwości przydzielenia, minimalizując odległość pomiędzy biórowcem i działką, oraz nie rozważam działek
#na pozycjach mniejszych od przydzielonej działki biórowcu X[i-1]. Algorytm ma złożoność O(n*m*logm).

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
  for i in range(1, n):
    for j in range(m):
      loc_dist = dist(X[i], Y[j])
      for x in range(j):
        DP[i][j] = min (DP[i][j], loc_dist + DP[i-1][x])
  # print(*DP, sep='\n')
  min_dist = DP[n-1][0]
  for j in range(m):
    min_dist = min(min_dist, DP[n-1][j])
  return min_dist
X = [3,6,10,14]
Y = [1,4,5,10,11,13,17]
print(parking(X, Y))
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
