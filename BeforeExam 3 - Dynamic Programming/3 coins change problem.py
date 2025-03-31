# We are given an array of numbers that represent each coin. The number of coins we have are infinity,
# so we do not need to worry about how many coins are at our disposal. Then we are given an amount and
# asked to find how many ways can we make the change.

def coin_change(coins, target):
    n = len(coins)
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1
    for coin in coins:
        for i in range(1, target + 1):
            if i >= coin:
                dp[i] += dp[i - coin]
    return dp[target]

total_money = 11
coins = [1, 2, 10]
print(coin_change(coins, total_money))