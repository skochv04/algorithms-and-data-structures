# Stas Kochevenko

# Opis: Spróbujmy przesuwać się po napisie-tablicy za pomocą zmiennej, która jest potencjalnym środkowym elementem
# szukanego najdłuższego palindromu. W każdej kolejnej iteracji wykorzystujemy zmienne lewej i prawej granicy tego
# palindromu, które będziemy przesuwali w pętli, dopóki nie osiągniemy końca tablicy lub nie przejdziemy
# granicy palindromu. W pętli liczymy długość, a po jej wykonaniu sprawdzamy, czy nie jest ta długość większa od tej,
# którą już mamy, jeśli tak, to zmieniamy wartość.
# Z treści zadania znamy, że szukamy palindrom o nieparzystej długości, więc dany algorytm wyszukiwa wyłącznie takie
# palindromy. W algorytmie są 2 pętli: zewnętrzna i wewnętrzna, każda wykonuje N iteracji, więc złożoność to O(N^2).

from zad1testy import runtests

def ceasar( s ):
    n = len(s)
    l_max = 1 #długość najdłuższego palindromu
    for i in range(n):
        left = i - 1
        right = i + 1
        l_loc = 1 #długość potencjalnego palindromu
        while left >= 0 and right < n and s[left] == s[right]:
            l_loc += 2
            left -= 1
            right += 1
        if l_loc > l_max:
            l_max = l_loc
    return l_max


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
