# Given set X of points on straight line. Find minimum number of closed unit intervals
# that are needed to cover all points from X.

def cover_points(X):
    n = len(X)
    X.sort()
    count = 1
    value = X[0]
    for i in range(n):
        if X[i] > value + 1:
            value = X[i]
            count += 1
    return count

X = [0.25, 0.5, 1.6, 1, 5, 2.3, 3.1, 4.5]
print(cover_points(X))