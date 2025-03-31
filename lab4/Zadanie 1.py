#Posortować n liczb {0 ... n^2 - 1}
#Będziemy robili radix sorta dla kubełków
from math import log10
def getDigit(num, i):
    return (num // 10**i) % 10

def sort_pom(T, digit):
    n = len(T)
    B = [0] * n
    C = [0] * 10
    for i in range(n):
        C[getDigit(T[i], digit)] += 1
    for i in range(1, 10):
        C[i] = C[i] + C[i-1]
    for i in range(n - 1, -1, -1):
        index = getDigit(T[i],digit)
        C[index]-=1
        B[C[index]] = T[i]
    for i in range (n):
        T[i]=B[i]


def radix(T):
    n = len(T)
    digit = 0
    leng = int(log10(n**2-1)) + 1
    for i in range(leng):
        sort_pom(T, digit)
        digit += 1



# T = [124, 403, 78, 94, 1, 404]
T = [2, 19, 24, 3, 7, 18]

radix(T)
print(T)
# print (getDigit(123, 0))