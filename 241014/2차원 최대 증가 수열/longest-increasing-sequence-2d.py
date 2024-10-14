n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(m):
    dp[0][i] = 1

for i in range(n):
    dp[i][0] = 1

for i in range(n):
    for j in range(m):

        ans = 1

        for k in range(i):
            for l in range(j):

                if not dp[k][l]:
                    continue

                if grid[k][l] >= grid[i][j]:
                    continue

                ans = max(ans, dp[k][l] + 1)

        
        dp[i][j] = ans
    
print(max(map(max, dp)))