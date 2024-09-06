dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

direction_mapper = {'U':1,'D':3,'R':0,'L':2}

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n


n, m, t = map(int, input().split())

grid = [[[] for _ in range(n)] for _ in range(n)]
temp_grid = [[[] for _ in range(n)] for _ in range(n)]

for i in range(m):

    r, c, d, w = input().split()

    r = int(r)
    c = int(c)
    w = int(w)

    r -= 1
    c -= 1

    grid[r][c].append((direction_mapper[d], w, i + 1))



for _ in range(t):

    for y in range(n):
        for x in range(n):
            for d, w, i in grid[y][x]:

                ny = y
                nx = x
                nd = d

                if not is_valid_coord(ny + dy[nd], nx + dx[nd]):
                    nd = (nd + 2) % 4
                else:
                    ny += dy[nd]
                    nx += dx[nd]

                temp_grid[ny][nx].append((nd, w, i))


    
    for y in range(n):
        for x in range(n):

            if len(temp_grid[y][x]) > 1:

                sum_weight = 0
                max_i = 0
                max_d = 0

                for d, w, i in temp_grid[y][x]:
                    sum_weight += w
                    
                    if i > max_i:
                        max_i = i
                        max_d = d

                temp_grid[y][x] = [(max_d, sum_weight, max_i)]



    for y in range(n):
        for x in range(n):
            grid[y][x] = temp_grid[y][x]

    for y in range(n):
        for x in range(n):
            temp_grid[y][x] = []

ans = 0

max_weight = 0


for i in range(n):
    for j in range(n):
        ans += len(grid[i][j])

        for _, w, _ in grid[i][j]:
            if w > max_weight:
                max_weight = w


print(ans, max_weight)