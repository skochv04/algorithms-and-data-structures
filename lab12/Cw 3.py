#Ladowanie promu
#F(i, g, d) = True, jeżeli pierwsze i aut da się rozdzielić tak, że na górnym pokładzie znajdą się auta zajmujące długość g, a na dolnym d
#F(i, g, d) = False, w przeciwnym przypadku

def rec(T, l1, l2, i=0):
    if i == len(T):
        return 0
    res1 = res2 = 0
    if l1 >= T[i]:
        res1 = rec(T, l1 - T[i], l2, i + 1) + 1
    if l2 >= T[i] and l2 != l1:
        res2 = rec(T, l1, l2 - T[i], i + 1) + 1
    return max(res1, res2)

def prom_0(T, l1, l2):
    n = len(T)
    dp = [[[False for _ in range(l2 + 1)] for _ in range(l1 + 1)] for _ in range(n + 1)]
    dp[0][0][0] = True
    last = -1
    for i in range(1, n + 1):
        for g in range(l1 + 1):
            for d in range(l2 + 1):
                if (g - T[i-1] >= 0 and dp[i-1][g - T[i-1]][d]) or (d - T[i-1] >= 0 and dp[i-1][g][d-T[i-1]]):
                    dp[i][g][d] = True
                    last = i-1
    return last

def prom(T, l1, l2):
    n = len(T)
    dp = [[False for _ in range(l1 + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    last = -1
    suma = 0
    for i in range(1, n + 1):
        for g in range(l1 + 1):
            d = suma - g
            if (g - T[i-1] >= 0 and dp[i-1][g - T[i-1]]):
                dp[i][g] = (g, d + T[i-1])
                last = (i, g, 1)
            elif d + T[i-1] <= l2 and dp[i-1][g]:
                last = (i, g, 0)
                dp[i][g] = (g, d + T[i-1])
        suma += T[i-1]
    # print(*dp, sep='\n')
    #


    # i, g, place = last
    # tab = []
    # if place == 1:
    #     while g != 0:
    #         tab.append(i - 1)
    #         g -= T[i-1]
    #         i -= 1
    #         while i > 0 and dp[i-1][g] != False:
    #             i -= 1
    # else:
    #     while g != 0:
    #         while i > 0 and dp[i - 1][g] != False:
    #             tab.append(i - 1)
    #             i -= 1
    #         g -= T[i - 1]
    #         i -= 1
    #
    # if g == 0 and i > 0 and dp[i - 1][g] != False:
    #     tab.append(i + 1)
    #     tab.append(i)
    #     while g == 0 and i > 0 and dp[i - 1][g] != False:
    #         tab.append(i - 1)
    #         i -= 1
    # return tab[::-1]
    return last

def my_prom(T, l1, l2):
    n = len(T)
    DP = [[False for b in range(l1 + 1)] for i in range(n)]
    parent = [[None for b in range(l1 + 1)] for i in range(n)]
    if T[0] <= l2:
        DP[0][0] = (0, T[0])
        parent[0][0] = (None, None, "D")
    if T[0] <= l1:
        DP[0][T[0]] = (T[0], 0)
        parent[0][T[0]] = (None, None, "G")
    last = -1
    for i in range(1, n):
        for b in range(l1 + 1):
            if b - T[i] >= 0 and DP[i-1][b - T[i]]:
                DP[i][b] = (b, DP[i-1][b - T[i]][1])
                parent[i][b] = (i-1, b - T[i], "G")
                last = (i, b)
            if DP[i-1][b] and DP[i-1][b][1] + T[i] <= l2:
                DP[i][b] = (b, DP[i-1][b][1] + T[i])
                parent[i][b] = (i-1, b, "D")
                last = (i, b)
    print(*DP, sep='\n')
    tab = None
    if last != -1:
        ind, pos = last #номер останнього, зайнята довжина
        type = parent[ind][pos][2] #верхній чи нижній? бо виводитемо тільки для одного
        tab = []
        ind, pos, loc_type = parent[ind][pos]
        while ind is not None and pos is not None:
            if loc_type == type:
                tab.append(ind+1)
            ind, pos, loc_type = parent[ind][pos]
        if ind is None and pos is None and loc_type == type:
            tab.append(0)

    return tab[::-1]
#
# T = [35, 0, 9, 6, 39, 32, 25, 48, 5, 22, 47, 6, 15, 28, 23, 4, 13, 20, 47, 10, 11, 6, 39, 48, 47, 26, 45, 40, 5, 48, 17, 2, 11,
#      6, 7, 26, 11, 12, 39, 2, 17, 2, 31, 36, 13, 38, 3, 38, 17, 42, 15, 48, 31, 14, 9, 34, 13, 28, 39, 0, 39, 8, 43, 38, 45, 16,
#      43, 36, 33, 24, 31, 46, 35, 36, 19, 2, 39, 38, 41, 14, 11, 14, 45, 12, 39, 4, 47, 22, 23, 46, 49, 22, 19, 22, 37, 44, 39, 2,
#      7, 22, 39, 40, 41, 16, 17, 20, 13, 46, 23, 8, 11, 30, 3, 40, 37, 46, 27, 14, 43, 2, 25, 30, 9, 20, 39, 12, 49, 32, 21, 2, 11,
#      26, 31, 24, 11, 46, 7, 6, 35, 26, 37, 30, 25, 10, 39, 36, 9, 42, 35, 32, 35, 30, 11, 48, 35, 28, 9, 2, 13, 32, 49, 8, 31, 46,
#      5, 20, 19, 24, 31, 14, 31, 34, 19, 10, 49, 46, 49, 34, 9, 40, 29, 18, 47, 40, 43, 28, 43, 18, 43, 6, 13, 4, 23, 36, 27, 24, 21,
#      14, 45, 28, 1, 36, 9, 24, 7, 10, 37, 18, 47, 28, 45, 36, 15, 36, 5, 2, 27, 8, 39, 12, 9, 16, 33, 42, 19, 14, 11, 4, 49, 42, 9,
#      6, 7, 20, 5, 46, 9, 20, 47, 28, 23, 28, 47, 28, 21, 26, 33, 48, 43, 48, 41, 44, 37, 22, 45, 4, 47, 32, 33, 36, 19, 12, 29, 42,
#      25, 24, 21, 8, 33, 20, 25, 0, 5, 6, 17, 16, 23, 32, 41, 0, 7, 14, 33, 40, 23, 4, 25, 36, 1, 46, 3, 18, 5, 32, 21, 32, 17, 24, 33, 14]
# l1 = 15
# l2 = 500
T = [5, 6, 1, 3, 2, 1, 3, 5]
l1 = 8
l2 = 10

print(my_prom(T, l1, l2))