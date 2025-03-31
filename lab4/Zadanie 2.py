#A - tablica, len(A) - n
#A = (a1, a2, ... an)
#Dla kazdego i ai nalezy do B. |B| = log(n)

# def counting (T):
#     n = len(T)
#     C = [(0, 0)] ????????? (log10(n)+1)
#     B = [0] * n
#     for x in T:
#         if x != 0:

#Mozna lepiej, N log log N, zeby bylo binarne
def translate(A):
    n = len (A)
    tab = []
    for i in range(n):
        test = True
        for j in range(len(tab)):
            if tab[j] == A[i]:
                A[i] = j
                test = False
                break
            if test:
                tab.append(A[i])
                A[i] = len(tab) - 1

