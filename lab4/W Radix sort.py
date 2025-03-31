#z inetu
def counting_sort(A, place):
    n = len(A)
    C = [0] * 10
    B = [0] * n
    for i in range(n):
        index = A[i] // place
        C[index % 10] += 1
    for i in range(1, 10):
        C[i] = C[i] + C[i-1]
    for i in range(n-1, -1, -1): #zachowujemy stabilność!!!
        index = A[i] // place
        B[C[index%10]-1] = A[i]
        C[index%10]-=1
    for i in range(n):
        A[i] = B[i]
    return B

def radixSort(A):
    max_element = max(A)
    place = 1
    while max_element // place > 0:
        counting_sort(A, place)
        place *= 10

data = [121, 432, 564, 23, 1, 45, 788]
radixSort(data)
print(data)