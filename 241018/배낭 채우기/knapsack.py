n, m = map(int, input().split())

goods = [(tuple(map(int, input().split()))) for _ in range(n)]

dp = [0 for _ in range(m + 1)]

for w, v in goods:
    for i in range(m, -1, -1):

        if i >= w:
            dp[i] = max(dp[i], dp[i - w] + v)


print(dp[m])