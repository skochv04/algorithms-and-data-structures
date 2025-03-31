# We are given a list of orders. Each order requires some starting capital C[i] which we will need to
# start the order and a profit P[i] which will add to our total capital when we execute the order.
# We get a starting capital W and a number k. Choose at most k orders so that you will end up with the
# maximum possible capital.
# Example: k = 2, P = [1, 2, 3], C = [0, 1, 1]. Solution: at the beginning we have capital 0, so we can
# choose only the first order. After its completion, we have a capital equal to 1, so we can choose either
# order 2 or 3. Order 3 has a bigger profit, so we choose order 3 because we can only choose one
# order (k = 2). We finish with capital of 4.

def orders(P, C, k):
    n = len(P)
    max_c = 0
    for i in range(n):
        max_c = max(max_c, C[i])
    T = [0 for _ in range(max_c + 1)]
    l = [(C[i], P[i]) for i in range(n)]
    l.sort(key=lambda x: x[1])
    for i, j in l:
        T[i] = max(T[i], j)
    W = 0
    for _ in range(k):
        i = 0
        max_order = 0
        while i < max_c + 1 and i <= W:
            max_order = max(max_order, W+T[i])
            i += 1
        W = max_order
    return W

k = 2
P = [1, 2, 3, 4, 8, 10, 11, 15, 1]
C = [0, 1, 1, 2, 2, 2, 3, 3, 4]
print(orders(P, C, k))