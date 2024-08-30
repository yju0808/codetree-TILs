n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

temp_grid = [[0 for _ in range(n)] for _ in range(n)]



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


def simul_bomb(y, x):

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


def copy_array(dest, origin):

    for i in range(n):
        for j in range(n):
            dest[i][j] = origin[i][j]


def get_score():
    
    score = 0

    for i in range(n):

        overlap_count = 0
        before = None

        for j in range(n):

            if grid[i][j] == 0:
                overlap_count = 0

            elif before == None:
                before = grid[i][j]
                overlap_count = 1

            elif grid[i][j] != before:
                if overlap_count == 2:
                    score += 1
                
                overlap_count = 1

            elif grid[i][j] == before:
                overlap_count += 1

            before = grid[i][j]

        
        if overlap_count == 2:
            score += 1

        

    for j in range(n):

        overlap_count = 0
        before = None

        for i in range(n):

            if grid[i][j] == 0:
                overlap_count = 0

            elif before == None:
                before = grid[i][j]
                overlap_count = 1

            elif grid[i][j] != before:
                if overlap_count == 2:
                    score += 1
                
                overlap_count = 1

            elif grid[i][j] == before:
                overlap_count += 1

            before = grid[i][j]

        if overlap_count == 2:
            score += 1

        

    return score
                

ans = 0

for i in range(n):
    for j in range(n):

        copy_array(temp_grid, grid)

        simul_bomb(i, j)
        simul_gravity()

        ans = max(ans, get_score())

        copy_array(grid, temp_grid)


print(ans)