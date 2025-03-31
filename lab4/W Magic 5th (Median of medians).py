def median(T, l, r):
    mid = (l+r-1)//2
    #print("mid: ")
    #print(mid-l+1)
    #print(l, end = ' ')
    #print(r)
    #print(T[l:r])
    for i in range(mid-l+1):
        mini = l+i
        j = l+i+1
        while(j < r):
            if(T[j] < T[mini]):
                mini = j
            j += 1
        #print(T[l:(r)])
        T[l+i], T[mini] = T[mini], T[l+i]
    #print("koniec: ")
    #print(T[l:(r)])
    return T[mid]
def podziel(T, r, T_wstaw):
    przed, ink = 0, 0
    #print("glowna: ")
    #print(T)
    while(przed + 5 <= r):
        T_wstaw[ink] = median(T, przed, przed+5)
        #print(T_wstaw)
        ink, przed = ink+1, przed+5
    if(r % 5 != 0):
        T_wstaw[ink] = median(T, przed, r)
    #print(T_wstaw)
    return T_wstaw

def piatki_rek(T, r, T_wstaw):
    if(r <= 5):
        return median(T, 0, r)
    T = podziel(T, r, T_wstaw)
    r = (r + 4) // 5
    #print("r: ")
    #print(r)
    return piatki_rek(T, r, T_wstaw)
def partition(T, l, r, mid):
    if(l >= r):
        return
    pivot = T[mid]
    T[mid], T[r] = T[r], T[mid]
    j = l
    for i in range(l, r, 1):
        if(T[i] < pivot):
            T[i], T[j] = T[j], T[i]
            j += 1
    T[j], T[r] =  T[r], T[j]
    #print(T)
    return j
def find_pivot(T, l , r, value):
    for i in range(l, r+1, 1):
        if(T[i] == value):
            return i
def find_kth_element(T_main, T_pom, n, k):
    l, r = 0, n - 1
    while (l < r):
        #length = (r - l + 1 + 4) // 5
        #print(length)
        T_part = T_main[l:(r + 1)]
        #print("przedzialy: ")
        #print(l, end=' ')
        #print(r)
        x = piatki_rek(T_part, r-l+1, T_pom)
        #print(T)
        #print("x: ")
        #print(x)
        pivot = find_pivot(T_main, l, r, x)
        #print("pivot: ")
        #print(pivot)
        pivot = partition(T_main, l, r, pivot)
        #print("pivot: ")
        #print(pivot)
        if (pivot == k):
            print("tablica po znalezieniu k - tego elementu")
            print(T_main)
            return T_main[k]
        elif(pivot < k):
            l = pivot+1
        else:
            r = pivot-1
    print("tablica po znalezieniu k - tego elementu")
    print(T_main)
    return T_main[k]
n = int(input())
T = [0] * n
for i in range(n):
    T[i] = int(input())
T_dodatkowa = [0] * ((n+4)//5)
k = int(input())
print("Tablica na poczatku: ")
print(T)
result = find_kth_element(T, T_dodatkowa, n, k)
print("wynik: ")
print(result)
#print(median(T, 0, n))