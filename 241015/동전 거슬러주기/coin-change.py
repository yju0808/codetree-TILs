import sys

sys.setrecursionlimit(10**5)

n, m = map(int, input().split())

coins = list(map(int, input().split()))

dp = [-1 for _ in range(m + 1)]

for coin in coins:
    if coin <= m:
        dp[coin] = 1


def get_answer(k):

    if k < 0:
        return float('inf')

    if dp[k] != -1:
        return dp[k]

    dp[k] = float('inf')

    for coin in coins:
        dp[k] = min(dp[k], get_answer(k - coin) + 1)

    return dp[k]

ans = get_answer(m)

print(ans if ans != float('inf') else -1)