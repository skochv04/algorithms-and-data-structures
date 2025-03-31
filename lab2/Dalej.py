# T[N]
# n nalezy {0, ....., N-1}
#
# i < j and T[i] > T[j]
# ile są takich par?

def pars(T):
    n = len (T)
    counter = 0
    for i in range (n):
        for j in range (i + 1, n):
            if T[i] > T[j]:
                counter += 1
    return counter

T = [29, 6, 13, 4]
print(pars(T))