#Mamy monety 2, 3, 5, 7 i t.d. i dla danej kwoty chcemy wydać jak najmniej monet
#Alg. zachłanny dla kwoty 15, monety 1, 5, 8 -> nie działa, nie można brać od największej do najmniejszej, bo opt to 3 5ki
import random
inf = float('inf')

#F(x) = minimalna liczba monet do wydania kwoty x
#F(0) = 0
#F(t) = inf dla t < 0
#F(x) = min F(x - m) + 1, m є T

# def coins(T, val):
#     F = [None for _ in range(val + 1)]
#     F[0] = 0
#     if val < 0:
#         return inf
#     if F[val] is None:
#         F[val] = min(coins(T, val-x, F) for x in T) + 1
#     return F[val]

def coins_dynamik(T, val):
    F = [inf for _ in range(val + 1)]
    F[0] = 0
    for i in range(val):
        for coin in T:
            if i + coin <= val:
                F[i+coin] = min(F[i+coin], F[i] + 1)
    return F

def second_coins_dynamik(T, val):
    F = [inf for _ in range(val + 1)]
    F[0] = 0
    for coin in T:
        F[coin] = 1
    for b in range(1, val + 1):
        for coin in T:
            if b - coin > 0:
                F[b] = min(F[b], F[b-coin] + 1)
    return F

n = 4
# T = [random.randint(1, 9) for _ in range(n)]
# T.sort()
# n = 3
T = [1, 5, 8]
val = 15
print(T, val)
# print(coins(T, val))
print(coins_dynamik(T, val))
print(second_coins_dynamik(T, val))