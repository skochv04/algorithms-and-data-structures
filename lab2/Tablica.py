# Mamy tablice A[N], liczby naturalne
# Mame x, szukamy 2 wartości, suma których jest równa x
def find_sum(T, x):
    n = len(T)
    i = 0
    j = n - 1
    while (i < j):
        if T[i] + T[j] == x:
            return True
        if T[i] + T[j] > x:
            j -= 1
        else:
            i += 1
    return False

T = [1, 2, 4, 5, 8, 10, 19]
print(find_sum(T, 29))

#Dane n przedziałów domkniętych, szukamy przedział, który zawiera jaknajwięcej innych
def find_obsz(T):
    n = len(T)
    count_i = max_ind = 0
    for i in (T):
        count_j = 0
        for j in (T):
            if i != j:
                if i[0] <= j[0] and i[1] >= j[1]:
                    count_j += 1
        if count_j > count_i:
            count_i = count_j
            max_ind = i
    return max_ind
T = [(1, 7), (2, 4), (3, 8), (1, 17), (2, 5), (4, 9), (1, 16), (9, 10)]
print (find_obsz(T))