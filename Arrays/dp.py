coins = [1, 4, 2, 6, 8]
target = 6

dp = [float('inf')] * (target +1)
dp[0] = 0

for total in range(1, target +1):
    for coin in coins:
        if coin <= total:
            dp[total] = min(dp[total], dp[total - coin] + 1)

print(dp[target])