#Zadania z terminami
#Починаємо від завдання з найбільш пізнім дедлайном, бо в день 0 можемо віддати будь-яке
#завдання, і обираємо серед тих які в цей день можемо віддати те, яке має найбільший кошт

def zadania(dni, g):
    n = len(dni)
    T = []
    for i in range(n):
        T.append((dni[i], zysk[i]))
    T.sort()
    print(T)
    tab = []
    time = max(dni)
    sum = 0
    for i in range(time, -1, -1): #day
        ind = i
        loc_max = T[i][1]
        j = len(T) - 1
        while j > 0 and T[j][0] >= i:
            if T[j][1] > loc_max:
                loc_max = T[j][1]
                ind = j
            j -= 1
        tab.append(T[ind])
        sum += loc_max
        T.pop(ind)
    return sum, tab

dni = [5, 1, 2, 4, 5, 3, 2]
zysk = [10, 1, 9, 7, 5, 3, 4]
print(zadania(dni, zysk))