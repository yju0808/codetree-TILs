


n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.insert(0, 0)




dp = [[[-float('inf') for _ in range(m + 1)] for _ in range(5)] for _ in range(n + 1)]

for i in range(5):
    dp[0][i][0] = 0

for i in range(1, n + 1):
    for j in range(1, 5):
        for k in range(1, 5):
            for l in range(m + 1):

                score = 1 if nums[i] == j else 0 

                if j == k:
                    dp[i][j][l] = max(dp[i][j][l], dp[i - 1][k][l] + score)
                else:
                    if l + 1 <= m:
                        dp[i][j][l +1] = max(dp[i][j][l + 1], dp[i - 1][k][l] + score)


ans = 0
for i in range(5):
    for j in range(m + 1):
        ans = max(ans, dp[n][i][j])

print(ans)
