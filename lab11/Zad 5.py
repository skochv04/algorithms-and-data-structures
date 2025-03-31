#Найдовший паліндром всередині строки (не послідовний?)
def findLongestPalindrome(X, i, j, lookup):
    # Base condition
    if i > j:
        return 0

    # If the string `X` has only one character, it is a palindrome
    if i == j:
        return 1

    # If the last character of the string is the same as the first character
    if lookup[i][j] == 0:
        if X[i] == X[j]:
            # include the first and last characters in palindrome
            # and recur for the remaining substring `X[i+1, j-1]`
            lookup[i][j] = findLongestPalindrome(X, i + 1, j - 1, lookup) + 2

    # Return the maximum of the two values
        else:
            lookup[i][j] = max(findLongestPalindrome(X, i, j - 1, lookup), findLongestPalindrome(X, i + 1, j, lookup))
    return lookup[i][j]


def findLongestPalindrome_bootomup(X):
     n = len(X)
     lookup = [[0 for i in range(n)] for j in range(n)]
     for i in range(n):
         lookup[i][i] = 1
     for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if X[i] == X[j]:
                lookup[i][j] = lookup[i+1][j-1] + 2
            else:
                lookup[i][j] = max(lookup[i][j-1], lookup[i+1][j])
     print(*lookup,sep='\n')
     return lookup[0][n-1]

X = 'aacaccabcc'
n = len(X)
lookup = [[0 for i in range(n)] for j in range(n)]
print('The length of the longest palindromic subsequence is', findLongestPalindrome(X, 0, n - 1, lookup))
print('The length of the longest palindromic subsequence is', findLongestPalindrome_bootomup(X))
