# There are n guilty people in a line, the i-th of them holds a claw with length L[i]. The bell rings
# and every person kills some of people in front of him. All people kill others at the same time.
# Namely, the i-th person kills the j-th person if and only if j < i and j >= i-L[i]. We are given
# lengths of the claws. We need to find the total number of alive people after the bell rings.

def wrath(L):
    n = len(L)
    T = [False for _ in range(n)]
    result = 1
    ind = n - 1
    for i in range(n-1, -1, -1):
        if i == ind:
            T[ind] = True
        ind = min(ind, i - L[i] - 1)
    result = 0
    for i in range(n):
        if T[i]:
            result += 1
    return result

L = [1, 0, 0, 1, 1, 3, 2, 0, 0, 2, 3]
print(wrath(L))