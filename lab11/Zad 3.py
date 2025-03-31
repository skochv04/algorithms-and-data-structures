#Знайти найбільший спільний для 2 рядків не обов'язково spójny підрядок.
#X: ABCBDAB
#Y: BDCABA
#The length of the LCS is 4
#LCS are BDAB, BCAB, and BCBA

def LCSLength_memoization(X, Y, m, n, lookup):
    # return if the end of either sequence is reached
    if m == 0 or n == 0:
        return 0

    # if the last character of `X` and `Y` matches
    if not lookup[m][n]:
        if X[m - 1] == Y[n - 1]:
            lookup[m][n] = LCSLength_memoization(X, Y, m - 1, n - 1, lookup) + 1

    # otherwise, if the last character of `X` and `Y` don't match
        else:
            lookup[m][n] = max(LCSLength_memoization(X, Y, m, n - 1, lookup), LCSLength_memoization(X, Y, m - 1, n, lookup))
    return lookup[m][n]


def LCSLength_bottom_up(X, Y):
    m = len(X)
    n = len(Y)

    # lookup table stores solution to already computed subproblems;
    # i.e., `T[i][j]` stores the length of LCS of substring
    # `X[0…i-1]` and `Y[0…j-1]`
    lookup = [[0 for x in range(n + 1)] for y in range(m + 1)]

    # fill the lookup table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if the current character of `X` and `Y` matches
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
            # otherwise, if the current character of `X` and `Y` don't match
            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])

    # LCS will be the last entry in the lookup table
    return lookup[m][n]


# Function to find the longest common subsequence of string `X[0…m-1]` and `Y[0…n-1]`
def LCS(X, Y, m, n, lookup):
    # return an empty string if the end of either sequence is reached
    if m == 0 or n == 0:
        return str()

    # if the last character of `X` and `Y` matches
    if X[m - 1] == Y[n - 1]:
        # append current character (`X[m-1]` or `Y[n-1]`) to LCS of
        # substring `X[0…m-2]` and `Y[0…n-2]`
        return LCS(X, Y, m - 1, n - 1, lookup) + X[m - 1]

    # otherwise, if the last character of `X` and `Y` are different

    # if a top cell of the current cell has more value than the left
    # cell, then drop the current character of string `X` and find LCS
    # of substring `X[0…m-2]`, `Y[0…n-1]`

    if lookup[m - 1][n] > lookup[m][n - 1]:
        return LCS(X, Y, m - 1, n, lookup)
    else:
        return LCS(X, Y, m, n - 1, lookup)

# if a left cell of the current cell has more value than the top
# cell, then drop the current character of string `Y` and find LCS
# of substring `X[0…m-1]`, `Y[0…n-2]`

X = 'ABCBDAB'
Y = 'BDCABA'
lookup = [[0 for x in range(len(Y)+1)] for y in range(len(X)+1)]
print('The length of the LCS is', LCSLength_memoization(X, Y, len(X), len(Y), lookup))
print('The length of the LCS is', LCSLength_bottom_up(X, Y))
print(LCS(X, Y, len(X), len(Y), lookup))
