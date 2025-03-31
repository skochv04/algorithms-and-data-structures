# Allen is hosting a formal dinner party. 2n people come to the event in n pairs (couples). After
# a night of fun, Allen wants to line everyone up for a final picture. The 2n people line up, but
# Allen doesn't like the ordering. Allen prefers if each pair occupies adjacent positions in the line,
# as this makes the picture more aesthetic. Help Allen find the minimum number of swaps of adjacent
# positions he must perform to make it so that each couple occupies adjacent positions in the line.

def suit_and_tie(T):
    swaps = 0
    n = len(T)

    # Перебираємо кожен елемент у списку
    for i in range(0, n, 2):
        # Перевіряємо, чи елементи на парних позиціях є парою
        if T[i] != T[i + 1]:
            # Шукаємо індекс наступного елемента, що утворює пару з поточним
            j = i + 2
            while j < n and T[j] != T[i]:
                j += 1
            if j < n and T[j] == T[i]:
                # Міняємо місцями елементи, щоб утворити пару
                T[i + 1], T[j] = T[j], T[i + 1]
                swaps += 1
    return swaps

n = 8
T = [7, 6, 2, 1, 4, 3, 3, 7, 2, 6, 5, 1, 8, 5, 8, 4]
print(suit_and_tie(T))