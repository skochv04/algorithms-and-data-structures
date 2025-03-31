#x є (0, 10^9 - 1) and Z
#Eksperyment wypluwa krótki ciąg z tego zakresu, mamy znależć ilość różnych liczb
#Wejscie: ciąg x1, ... xn
#Wyjscie: ile jest różnych liczb

def counting_sort(A, k):
    n = len(A)
    C = [0] * k
    B = [0] * n
    for i in range(n):
        C[A[i]] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    for i in range(n-1, -1, -1): #zachowujemy stabilność!!!
        B[C[A[i]]-1] = A[i]
        C[A[i]]-=1
    for i in range(n):
        A[i] = B[i]
    return B