n = int(input())

nums = list(map(int, input().split()))

dp = [-1 for _ in range(n)]
dp[0] = 0
ans = 0

for i in range(1, n):
    for j in range(0, i):
        
        if dp[j] == -1:
            continue
            
        dist = nums[j]

        if j + dist < i:
            continue

        dp[i] = max(dp[j] +1, dp[i])

print(max(dp))