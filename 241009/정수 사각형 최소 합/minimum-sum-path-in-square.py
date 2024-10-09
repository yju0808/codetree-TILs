n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][n - 1] = grid[0][n - 1]

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n

def get_answer(i, j):

    if dp[i][j]:
        return dp[i][j]

    ans = float('inf')

    if is_valid_coord(i - 1, j):
        ans = min(ans, get_answer(i - 1, j))

    if is_valid_coord(i, j + 1):
        ans  = min(ans, get_answer(i, j + 1))

    dp[i][j] = ans + grid[i][j]
    return dp[i][j]


print(get_answer(n - 1, 0))