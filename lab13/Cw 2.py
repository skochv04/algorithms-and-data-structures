#Pokrycie przedziałami jednostkowymi.
#Na przykład, dla X = {0.25, 0.5, 1.6} potrzebne są dwa przedziały,
#mogą to być [0.2, 1.2], oraz [1.4, 2.4]

def przedzialy(P):
    P.sort()
    P = P[::-1]
    licznik = 0

    while P:
        start = P[-1]
        while start <= P[-1] <= start + 1:
            P.pop()

        licznik += 1

    return licznik

X = [0.25, 0.5, 1.6]
print(przedzialy(X))