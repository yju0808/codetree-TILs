


n = int(input())

nums = [0 for _ in range(10)]

dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(n + 1)]


info = [tuple(map(int, input().split())) for _ in range(n)]
info.insert(0, (0,0,0))

for i in range(0, 3):
    dp[1][i] [i]= info[1][i]


for i in range(2, n + 1):
    for j in range(3):
        for k in range(3):
            for l in range(3):

                if k != l:
                    dp[i][j][k] = max(dp[i][j][k],  dp[i - 1][j][l] + info[i][k])



ans = 0

for i in range(3):
    for j in range(3):
        if i != j:
            ans = max(ans, dp[n][i][j])

print(ans)