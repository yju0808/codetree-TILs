n = int(input())

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]


def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n

def can_gone(y1, x1, y2, x2):
    if grid[y1][x1] <= grid[y2][x2]:
        return True

    return False

def get_answer(y, x):
    
    if dp[i][j]:
        return dp[i][j]

    for i in range(4):

        ny = y + dy[i]
        nx = x + dx[i]

        if is_valid_coord(ny, nx) and can_gone(y, x, ny, nx):