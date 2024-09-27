n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

direction = [list(map(int, input().split())) for _ in range(n)]



def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n


dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]


ans = 0

def solve(y, x, count):

    global ans

    ans = max(ans, count)

    d = direction[x][y] - 1

    for i in range(n):
        nx, ny = x + dxs[d] * i, y + dys[d] * i

        if is_valid_coord(ny, nx) and grid[ny][nx] > grid[y][x]:
            solve(ny, nx, count + 1)


y, x = map(int, input().split())

y -= 1
x -= 1

solve(y, x, 0)
print(ans)