# Igor found out discounts in a shop and decided to buy n items. Discounts at the store will last for
# a week and Igor knows about each item that its price now is a[i], and after a week of discounts its
# price will be b[i]. Not all of sellers are honest, so now some products could be more expensive than
# after a week of discounts. Igor decided that buy at least k of items now, but wait with the rest of
# the week in order to save money as much as possible. Your task is to determine the minimum money that
# Igor can spend to buy all n items.

def dishonest_sellers(n, k, a, b):
    T = []
    for i in range(n):
        T.append((a[i] - b[i], i))
    T.sort(key=lambda x: x[0])
    sum = 0
    for i in range(k):
        sum += a[T[i][1]]
    i = k
    while i < n and T[i][0] <= 0:
        sum += a[T[i][1]]
        i += 1
    for j in range(i, n):
        sum += b[T[j][1]]
    return sum

a = [87, 96, 19, 81, 10, 88, 7, 49, 36, 21]
b = [11, 75, 28, 28, 74, 17, 64, 19, 81, 31]
n, k = 10, 5
print(dishonest_sellers(n, k, a, b))