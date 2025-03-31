#Найдовший повторюваний підрядок (незв'язний), який присутній у рядку принаймні двічі

# Function to find the length of the longest repeated subsequence
# of substring `X[0…m-1]` and `X[0…n-1]`
def LRSLength(X, m, n):
    # return if the end of either string is reached
    if m == 0 or n == 0:
        return 0

    # if characters at index `m` and `n` matches and the index are different
    if X[m - 1] == X[n - 1] and m != n:
        return LRSLength(X, m - 1, n - 1) + 1

    # otherwise, if characters at index `m` and `n` don't match
    return max(LRSLength(X, m, n - 1), LRSLength(X, m - 1, n))

def LRSLength_bottomup(X, m, n):
    lookup = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == X[j-1] and i != j:
                lookup[i][j] = lookup[i-1][j-1] + 1
            else:
                lookup[i][j] = max(lookup[i][j-1], lookup[i-1][j])
    return lookup[m][n]


X = 'ATACTCGGA'
#ATaCtcGga
#atAcTCgGa
m = len(X)

print('The length of the longest repeating subsequence is', LRSLength(X, m, m))
print('The length of сthe longest repeating subsequence is', LRSLength_bottomup(X, m, m))