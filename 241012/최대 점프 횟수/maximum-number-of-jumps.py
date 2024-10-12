n = int(input())
nums = list(map(int, input().split()))
dp = [-1 for _ in range(n)]
dp[0] = 0  # 시작 위치는 점프 횟수 0으로 초기화

def dfs(i):
    if dp[i] != -1:
        return dp[i]
    max_jumps = -1
    for j in range(i):
        if dfs(j) == -1:
            continue
        if j + nums[j] >= i:
            max_jumps = max(max_jumps, dp[j] + 1)
    dp[i] = max_jumps
    return dp[i]

for i in range(1, n):
    dfs(i)

print(max(dp))