n, m, q = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

result_grid = [[0 for _ in range(m)] for _ in range(n)]



for i in range(n):
    for j in range(m):
        result_grid[i][j] = grid[i][j]

def rotate(r1, c1, r2, c2):
    
    temp = grid[r1][c2]
    for i in range(c2, c1, -1):
        grid[r1][i] = grid[r1][i - 1]
    
    temp2 = grid[r2][c2]
    for i in range(r2, r1, -1):
        grid[i][c2] = grid[i - 1][c2]
    
    if is_valid_coord(r1 + 1, c2):
        grid[r1 + 1][c2] = temp
    
    temp = grid[r2][c1]
    for i in range(c1, c2):
        grid[r2][i] = grid[r2][i + 1]

    if is_valid_coord(r2, c2 - 1):
        grid[r2][c2 - 1] = temp2

    for i in range(r1, r2):
        grid[i][c1] = grid[i + 1][c1]

    if is_valid_coord(r2 - 1, c1):
        grid[r2 - 1][c1] = temp
    
    
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < m

def make_avg(r1, c1, r2, c2):

    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):

            new = grid[i][j]
            count = 1

            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]

                if is_valid_coord(ny, nx):
                    count += 1
                    new += grid[ny][nx]
            
            result_grid[i][j] = int(new / count)




for _ in range(q):

    r1, c1, r2, c2 = map(int, input().split())

    c1 -= 1
    c2 -= 1
    r1 -= 1
    r2 -= 1

    rotate(r1, c1, r2, c2)

    for i in range(n):
        for j in range(m):
            result_grid[i][j] = grid[i][j]

    make_avg(r1, c1, r2, c2)

    for i in range(n):
        for j in range(m):
            grid[i][j] = result_grid[i][j]


for row in grid:
    print(*row)