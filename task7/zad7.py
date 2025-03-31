#Stas Kochevenko
#Opis: W głównej funkcji tworzymy tablicę rozmiarem n*n o wartościach -1 i zwrócamy wynik działania funkcji path dla
#tablicy L oraz nowej tablicy tab. Funkcja path zwraca maksymlną liczbę komnat, które można odwiedzić z danego miejsca.
#Dane te zapisujemy do pomocniczej tablicy tab, żeby nie wykonywać tego samego wielokrotnie. Jeśli w tablicy jeszcze nie
#ma wartości różnej od -1, to wpisujemy maksymalną liczbe komnat pomiędzy opcjami góra/dół/prawo.

from zad7testy import runtests
inf = float('inf')

def go_up(L, w, k):
    sum = 0
    while w > 0 and L[w-1][k] != '#':
        sum += 1
        w-=1
    if k < len(L) - 1:
        while w < len(L) - 1 and L[w][k+1] == '#' and sum != 0:
            sum -= 1
            w+=1
    return sum, w

def go_down(L, w, k):
    sum = 0
    while w < len(L)-1 and L[w+1][k] != '#':
        sum += 1
        w+=1
    if k < len(L) - 1:
        while w > 0 and L[w][k+1] == '#' and sum != 0:
            sum -= 1
            w-=1
    return sum, w

def path(L, tab, w = 0, k = 0):
    n = len(L)
    if w == k == n - 1:
        return 0
    if k > n - 1 or L[w][k] == '#':
        return -1
    if k == n - 1:
        down, w_down = go_down(L, w, k)
        if w_down == n - 1:
            return down
        return -1
    if tab[w][k] == -1:
        up, w_up = go_up(L, w, k)
        down, w_down = go_down(L, w, k)
        a = path(L, tab, w_up, k + 1)
        b = path(L, tab, w_down, k + 1)
        tab[w][k] = max(a + up, b + down)
        if tab[w][k] != -1:
            tab[w][k] += 1
    return tab[w][k]

def maze( L ):
    n = len(L)
    tab = [[-1 for _ in range(n)] for _ in range(n)]
    return path(L, tab)

L = ['....', '..#.', '..#.', '....']
L0 = ['......', '#..#..', '.#..#.', '##..#.', '......', '......']
L1 = ['....#...##',
      '...#....##',
      '#.........',
      '.......#..',
      '.......##.',
      '...#....#.',
      '#....#....',
      '##.....#.#',
      '..........',
      '......#...']

print(*L1, sep='\n')
print(maze(L1))
#94
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
