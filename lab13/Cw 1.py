#Problem stacji benzynowych
#Traktor jedzie z A do B, spala 1 litr paliwa na jeden km.
#W baku mieści się L litrów, na trasie są stacje benzynowe (na pozycjach gdzie są liczby naturalne).
#A jest na pozycji 0, zadanie:

#1 - wyznaczyć stacje, na których tankujemy tak, żeby tankowań było jak najmniej
def stacje_1(L, S):
    n = len(S)

    stations = [0]
    pos = L

    while pos < n-1:
        i = pos
        while i >= pos - L and S[i] is None:
            i -= 1

        stations.append(i)
        pos += L - (pos - i)
    return stations

#2 - żeby kosz przejazdu był minimalny, możemy tankować dowolną liczbę paliwa
def stacje_2(L, S):
    pos = 0
    N = len(S)
    fuel = 0
    price = 0
    while pos < N:
        cheapest = sorted([x for x in enumerate(S)[pos:pos + L] if x[1]], key=lambda x: x[1])[0]
        if cheapest[0] == pos:
            need = min(L - fuel, N - pos - fuel)
            price += need * cheapest[1]
            fuel += need
            pos = min(L, N - pos)
        else:
            dist = cheapest[0] - pos
            need = max(0, dist - fuel)
            fuel += need
            price += need * S[pos]
            pos += dist
    return price

#3 jesli na stacji tankujemy, to musimy zatankować do pełna


def my_first(L, T):
    n = len(T)
    pos = L
    prev = 0
    tab = [0]
    while pos < n - 1:
        while pos > prev and T[pos] is None:
            pos -= 1
        if pos > prev and T[pos] is not None:
            tab.append(pos)
            prev = pos
            pos += L
        else:
            return None
    return tab


def my_second(L, T):
    n = len(T)
    koszt = 0
    pos = 0
    while pos < n - 1:
        aim = min(n - 1, pos + L)
        loc_price = T[pos]
        for i in range(pos + 1, min(pos + L + 1, n)):
            if T[i] < loc_price:
                loc_price = T[i]
                aim = i
        koszt += T[pos] * (aim - pos)
        pos = aim
    return koszt

# T = [None, None, 12, None, None, 52, None]
# print(my_first(4, T))

T = [1, 9, 4, 2, 10, 13, 7]
print(stacje_2(4, T))