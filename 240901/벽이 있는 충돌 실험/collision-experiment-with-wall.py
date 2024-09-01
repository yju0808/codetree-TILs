t = int(input())

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

direction_mapper = {'U':1,'D':3,'R':0,'L':2}

def is_valid_coord(y, x, n):
    return 0 <= y < n and 0 <= x < n


for _ in range(t):

    n, m = map(int, input().split())

    grid = [[-1 for _ in range(n)] for _ in range(n)]
    temp_grid = [[-1 for _ in range(n)] for _ in range(n)]

    for _ in range(m):

        y, x, d = input().split()

        y = int(y)
        x = int(x)
        y -= 1
        x -= 1

        grid[y][x] = direction_mapper[d]

    for _ in range(n * n):
        
        for y in range(n):
            for x in range(n):

                if grid[y][x] >= 0:
                    
                    d = grid[y][x]

                    ny = y + dy[d]
                    nx = x + dx[d]

                    # 벽에 부딧히는 경우
                    if not is_valid_coord(ny, nx, n):

                        if temp_grid[y][x] >= 0:
                            temp_grid[y][x] = -1
                            
                        else:
                            temp_grid[y][x] = (d + 2) % 4

                    # 구슬끼리 충돌하는 경우
                    elif temp_grid[ny][nx] >= 0:
                        temp_grid[ny][nx] = -1

                    # 문제 없는 경우
                    elif temp_grid[ny][nx] == -1:
                        temp_grid[ny][nx] = d


        for i in range(n):
            for j in range(n):
                grid[i][j] = temp_grid[i][j]

        for i in range(n):
            for j in range(n):
                temp_grid[i][j] = -1


    ans = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 0:
                ans += 1
    
    print(ans)