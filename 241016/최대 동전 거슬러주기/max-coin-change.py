n, m = map(int, input().split())

coins = list(map(int, input().split()))

dp = [0 for _ in range(m + 1)]

for i in range(1, m +1):
    for coin in coins:
        if i >= coin:
            dp[i] = max(dp[i], dp[i - coin] +1)

print(dp[m] if dp[m] != 0 else -1)