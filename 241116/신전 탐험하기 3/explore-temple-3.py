


n, m  = map(int, input().split())

nums = [0 for _ in range(10)]

dp = [[0 for _ in range(m)] for _ in range(n + 1)]


info = [tuple(map(int, input().split())) for _ in range(n)]
info.insert(0, (0 for _ in range(m)))

for i in range(m):
    dp[1][i] = info[1][i]


for i in range(2, n + 1):
    for j in range(m):
        for k in range(m):

            if j != k:
                dp[i][j] = max(dp[i][j],  dp[i - 1][k] + info[i][j])



ans = 0

for i in range(m):
    ans = max(ans, dp[n][i])

print(ans)