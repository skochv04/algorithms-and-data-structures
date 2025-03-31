#Algorytm realizający domknięcie przychodni (транзитивного замикання) w grafie skierowanym w postaci macierzowej.
#Типу як об'єднання [1; 3] + [2; 3] = [1; 3]
#З використанням Флойда-Варшала

def domkn(G):
    n = len(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                G[i][j]=(G[i][k] and G[k][j]) or G[i][j]
    return G

T = True
F = False
G = [[F, T, F, F],
     [F, F, T, F],
     [T, F, F, T],
     [F, F, F, F]]

print(domkn(G))