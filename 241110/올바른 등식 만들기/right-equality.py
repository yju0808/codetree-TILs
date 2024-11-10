n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.insert(0, 0)

dp = [[0 for _ in range(41)] for _ in range(len(nums) + 1)]
dp[0][20] = 1

for i in range(1, len(nums)):
    for j in range(41):

        current_num = nums[i]

        if j + current_num <= 40:
            dp[i][j] += dp[i - 1][j + current_num]

        if j - current_num >= 0:
            dp[i][j] += dp[i - 1][j - current_num]

print(dp[n][m + 20])