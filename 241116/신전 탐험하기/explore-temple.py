


n = int(input())

nums = [0 for _ in range(10)]

dp = [[0 for _ in range(3)] for _ in range(n + 1)]


info = [tuple(map(int, input().split())) for _ in range(n)]
info.insert(0, (0,0,0))

for i in range(0, 3):
    dp[1][i] = info[1][i]


for i in range(2, n + 1):
    for j in range(3):
        for k in range(3):

            if j != k:
                dp[i][j] = max(dp[i][j],  dp[i - 1][k] + info[i][j])



ans = 0

for i in range(3):
    ans = max(ans, dp[n][i])

print(ans)