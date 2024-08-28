n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]



dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n


def simul_gravity():
    
    for j in range(n):

        index = n - 1
        keep = 0

        for i in range(n - 1, -1, -1):

            if grid[i][j] == 0:
                continue

            if keep == 0:
                keep = grid[i][j]

            elif grid[i][j] != 0:
                grid[index][j] = keep
                keep = grid[i][j]
                index -= 1

        if keep != 0:
            grid[index][j] = keep

        for i in range(index - 1, -1, -1):
            grid[i][j] = 0


def simul_bomb(col):

    col -= 1
    y, x = -1, col

    for i in range(n - 1, -1, -1):
        if grid[i][col] != 0:
            y, x = i, col

    if y == -1:
        return

    count = grid[y][x]
    grid[y][x] = 0

    for i in range(4):

        ny = y
        nx = x

        for _ in range(count - 1):

            ny += dy[i]
            nx += dx[i]

            if is_valid_coord(ny, nx):
                grid[ny][nx] = 0


            

for _ in range(m):
    c = int(input())

    simul_bomb(c)
    simul_gravity()


for row in grid:
    print(*row)