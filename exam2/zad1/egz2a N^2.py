#Stas Kochevenko
#Rozwiązanie o złożoności kwadratowej polega na tym, że dla każdego punktu z tablicy P znajdujemy maksumalną licbę
#punktów, nad którymi dominuje rozważany punkt. W wyniku działania algorytmu zwrócamy maksymalną silę spośród sił
#każdego punktu.

from egz2atesty import runtests

def dominance(P):
  n = len(P)
  sila = 0
  for i in range(n):
    loc_sila = 0
    for j in range(n):
      if P[j][0] < P[i][0] and P[j][1] < P[i][1]:
        loc_sila += 1
    sila = max(sila, loc_sila)
  return sila

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
