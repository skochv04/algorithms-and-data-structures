def insertion_sort(T):
    n = len(T)
    for i in range(1, n):
        while i > 0 and T[i] < T[i-1]:
            T[i], T[i-1] = T[i-1], T[i]
            i -= 1

def bucket_sort(T):
    num = 10
    A = [[] for i in range(num)]
    for i in T:
        index = int(i * num)
        A[index].append(i)
    for i in range(num):
        insertion_sort(A[i])
    k = 0
    for i in range(num):
        for j in range(len(A[i])):
            T[k] = A[i][j]
            k += 1
    return T



T = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
bucket_sort(T)
print(T)