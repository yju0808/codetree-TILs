n = int(input())

nums = list(map(int, input().split()))

dp = [[1, 1] for _ in range(n)]

for i in range(1, n):
    for j in range(i):

        if nums[i] > nums[j]:
            dp[i][0] = max(dp[i][0], dp[j][0] +1)

        elif nums[i] < nums[j]:
            dp[i][1] = max(dp[i][1], dp[j][1] + 1)

    dp[i][1] = max(dp[i][0], dp[i][1])

print(max(map(max, dp)))