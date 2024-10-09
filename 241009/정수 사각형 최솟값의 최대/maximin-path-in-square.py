n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = grid[0][0]

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n

def get_answer(i, j):

    if dp[i][j]:
        return dp[i][j]

    ans = -1

    if is_valid_coord(i - 1, j):
        ans = max(get_answer(i - 1,  j), ans)

    if is_valid_coord(i, j - 1):
        ans = max(get_answer(i, j -1), ans)

    dp[i][j] = min(grid[i][j], ans)
    return dp[i][j]


print(get_answer(n - 1, n - 1))