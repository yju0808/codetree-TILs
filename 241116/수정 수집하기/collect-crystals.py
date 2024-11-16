
n, k_ = map(int, input().split())

directions = input()

directions = 'X' + directions


dp = [[[-float('inf') for _ in range(k_ + 1)] for _ in range(2)] for _ in range(n + 1)]
dp[1][0][0] = 1 if directions[1] ==' L' else 0
dp[1][1][0] = 1 if directions[1] == 'R' else 0

for i in range(2, n + 1):
    for j in range(2):
        for k in range(2):
            for l in range(k_ + 1):

                cristal = 0
                d = directions[i]

                if (j == 0 and d == 'L') or (j == 1 and d == 'R'):
                    cristal = 1

                if j == k:
                    dp[i][j][l] = max(dp[i][j][l], dp[i - 1][k][l] + cristal)
                else:

                    if l + 1 <= k_:
                        dp[i][j][l +1] = max(dp[i][j][l + 1], dp[i - 1][k][l] + cristal)

ans = 0
for i in range(2):
    for j in range(k_ + 1):
        ans = max(ans, dp[n][i][j])


print(ans)
