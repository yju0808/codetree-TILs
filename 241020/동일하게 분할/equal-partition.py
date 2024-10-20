n = int(input())

nums = list(map(int, input().split()))

nums.insert(0, 0)

m = sum(nums)

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
dp[0][0] = True


for i in range(1, n + 1):
    for j in range(m + 1):

        if j >= nums[i] and dp[i - 1][j - nums[i]]:
            dp[i][j] = True

        if dp[i - 1][j]:
            dp[i][j] = True


ans = 'No'

for i in range(1, m):
    if dp[n][i]:
        if i == m // 2:
            ans = 'Yes'
        

print(ans)