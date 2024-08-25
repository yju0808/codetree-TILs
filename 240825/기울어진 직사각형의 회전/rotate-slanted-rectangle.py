N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]

result_grid = [[0 for _ in range(N)] for _ in range(N)]


dy = [-1, -1, 1, 1]
dx = [1, -1, -1, 1]

def is_vaild_coord(y, x):
    return 0 <= y < N and 0 <= x < N 

for i in range(N):
    for j in range(N):
        result_grid[i][j] = grid[i][j]


def do_something(y, x, m1, m2, m3, m4, dir_):

    result = 0
    move = [m1, m2, m3, m4]

    for i in range(4):
        for _ in range(move[i]):
            y += dy[i]
            x += dx[i]


            if dir_ == 0:
                pass
                result_grid[y][x] = grid[y - dy[i]][x - dx[i]]
            else:
                pass
                result_grid[y - dy[i]][x - dx[i]] = grid[y][x]




r, c, m1, m2, m3, m4, dir_ = map(int, input().split())

r -= 1
c -= 1

do_something(r, c, m1, m2, m3, m4, dir_)

for row in result_grid:
    print(*row)