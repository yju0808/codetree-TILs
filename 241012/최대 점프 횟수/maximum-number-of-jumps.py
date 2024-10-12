n = int(input())

nums = list(map(int, input().split()))

dp = [0 for _ in range(n)]

ans = 0

for i in range(1, n):
    for j in range(i, -1, -1):
        
        dist = nums[j]
        if j + dist < i:
            continue

        dp[i] = max(dp[j] +1, dp[i])

print(dp[n - 1])