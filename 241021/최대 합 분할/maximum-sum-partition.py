n = int(input())

nums = list(map(int, input().split()))
offest = 100000

nums.insert(0, 0)

m = sum(nums)

dp = [[0 for _ in range(m + 1 +offest)] for _ in range(n + 1)]
dp[0][0] = True


for i in range(n +1):
    for j in range(-m, m + 1):
        dp[i][j +offest] = -float('inf')


    dp[0][0 + offest] = 0

def update(i, j, prev_i, prev_j, val):
    if prev_j < -m or prev_j > m or dp[prev_i][prev_j + offest] == -float('inf'):
        return
    
    dp[i][j + offest] = max(dp[i][j + offest], dp[prev_i][prev_j + offest] + val)



for i in range(1, n + 1):
    for j in range(-m, m + 1):
        update(i, j, i - 1, j - nums[i], nums[i])

        update(i, j, i - 1, j + nums[i], 0)

        update(i, j, i  - 1, j, 0)

print(dp[n][0 + offest])