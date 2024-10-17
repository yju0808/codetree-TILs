n, m = map(int, input().split())

nums = list(map(int, input().split()))
dp = [float('inf') for _ in range(m + 1)]
dp[0] = 1


for num in nums:
    for i in range(m, -1, -1):
        if i >= num:
            dp[i] = min(dp[i], dp[i - num] + 1)

print('Yes' if dp[m] != float('inf') else 'No')