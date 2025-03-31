#Sortowanie kopcowe / Heap sort
#Kopiec - drzewo binarne, w którym każdy węzel wewnętrzny przechowuje wartość większą lub równą niż jego dzieci
#left = 2i+1, right = 2i + 2, parent = (i - 1)/2

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def heapify(T, i, n):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and T[l] > T[max_ind]:
        max_ind = l
    if r < n and T[r] > T[max_ind]:
        max_ind = r
    if max_ind != i:
        T[i], T[max_ind] = T[max_ind], T[i]
        heapify(T, max_ind, n)

def heap_build(T):
    n = len(T)
    for i in range(parent(n - 1), -1, -1):
        heapify(T, i, n)

def heap_sort(T):
    n = len(T)
    heap_build(T)
    for i in range(n - 1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, 0, i)

#W3
#insert - wstaw element
#extract_max - wyjmij element największy

def insert (T, value):
    T.append(value)
    n = len(T) - 1
    while T[parent(n)] < T[n]:
        T[parent(n)], T[n] = T[n], T[parent(n)]
        n = parent(n)

def extract_maximum (T):
    n = len(T)
    T[0], T[n - 1] = T[n - 1], T[0]
    T.pop()
    heapify(T, 0, n-1)

T = [12, 6, 13, 44, 8, 7, 1]
# heap_sort(T)
insert(T, 29)
heap_build(T)
print (T)
extract_maximum(T)
print(T)