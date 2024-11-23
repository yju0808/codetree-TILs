

n, m = map(int, input().split())

nums = list(map(int, input().split()))

nums.insert(0, 0)

dp = [[[0 for _ in range(2)] for _ in range(m + 1)] for _ in range(n + 1)]


for i in range(0, n + 1):
    for j in range(0, m + 1):
        dp[i][j][0] = - float('inf')
        dp[i][j][1] = -float('inf')

for i in range(0, n + 1):
    dp[i][0][0] = 0


for i in range(1, n + 1):
    for j in range(1, m + 1):
        
        dp[i][j][1] = max(dp[i - 1][j - 1][0] + nums[i], dp[i - 1][j][1] + nums[i])

        dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1])


print(max(dp[n][m][0], dp[n][m][1]))

