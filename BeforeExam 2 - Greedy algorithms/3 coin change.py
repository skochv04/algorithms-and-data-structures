# Given an array of numbers that represent each coin. The number of coins we have are
# infinity, so we do not need to worry about how many coins are at uor disposal. Then
# we are given an amount and asked to find the minimum number of coins that are needed
# to make that amount.

def coin_change(coins, amount):
    coins.sort()
    coins = coins[::-1]
    last = amount
    used = 0
    i = 0
    while i < len(coins):
        if last - coins[i] >= 0:
            last -= coins[i]
            used += 1
        else:
            i += 1
    return used

amount = 237
coins = [1, 10, 100, 25, 5]
print(coin_change(coins, amount))