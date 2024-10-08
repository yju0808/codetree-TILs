dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

direction_mapper = {'U':1,'D':3,'R':0,'L':2}

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n


n, m, t, k = map(int, input().split())

grid = [[[] for _ in range(n)] for _ in range(n)]
temp_grid = [[[] for _ in range(n)] for _ in range(n)]

for i in range(m):

    r, c, d, v = input().split()

    r = int(r)
    c = int(c)
    v = int(v)

    r -= 1
    c -= 1

    grid[r][c].append((direction_mapper[d], v, i + 1))



for _ in range(t):

    for y in range(n):
        for x in range(n):
            for d, v, i in grid[y][x]:

                ny = y
                nx = x
                nd = d

                for _ in range(v):
                    if not is_valid_coord(ny + dy[nd], nx + dx[nd]):
                        nd = (nd + 2) % 4

                    ny += dy[nd]
                    nx += dx[nd]

                temp_grid[ny][nx].append((nd, v, i))


    
    for y in range(n):
        for x in range(n):

            if len(temp_grid[y][x]) > k:

                temp_grid[y][x].sort(lambda x: (-x[1], -x[2]))
                rest = temp_grid[y][x][:k]
                temp_grid[y][x] = rest



    for y in range(n):
        for x in range(n):
            grid[y][x] = temp_grid[y][x]

    for y in range(n):
        for x in range(n):
            temp_grid[y][x] = []

ans = 0

for i in range(n):
    for j in range(n):
        ans += len(grid[i][j])


print(ans)