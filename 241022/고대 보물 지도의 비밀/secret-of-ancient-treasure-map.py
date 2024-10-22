n, k = map(int, input().split())

nums = list(map(int, input().split()))

nums.insert(0, 0)

dp = [[-float('inf') for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(k + 1):
    dp[0][i] = 0

for i in range(1, n + 1):

    if nums[i] >= 0:
        for j in range(0, k + 1):
            dp[i][j] = max(nums[i], dp[i - 1][j] + nums[i])

    else:
        for j in range(1, k + 1):
            dp[i][j] = max(dp[i - 1][j - 1] + nums[i], nums[i])



ans = -float('inf')


for i in range(n + 1):
    for j in range(k +1):
        ans = max(ans, dp[i][j])

print(ans)