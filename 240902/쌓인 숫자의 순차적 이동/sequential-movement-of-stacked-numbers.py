n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        grid[i][j] = [grid[i][j]]


def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n


def get_number_index(number):
    for i in range(n):
        for j in range(n):
            for k in range(len(grid[i][j])):
                if grid[i][j][k] == number:
                    return (i, j, k)
        
    return None


def get_max_number_index(y, x):

    max_num = 0
    ans_y, ans_x = 0, 0

    for i in range(8):

        ny = y + dy[i]
        nx = x + dx[i]

        if is_valid_coord(ny, nx):
            for k in grid[ny][nx]:
                if k >= max_num:
                    ans_y, ans_x = ny, nx
                    max_num = k
                    
        
    return ans_y, ans_x


dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [1, 1, 0, -1, -1, -1, 0, 1]


numbers = list(map(int, input().split()))


for number in numbers:
    
    y, x, k = get_number_index(number)
    ny, nx = get_max_number_index(y, x)

    a = grid[y][x][k:]
    b = grid[y][x][:k]
    grid[y][x] = b

    grid[ny][nx].extend(a)




    
for i in range(n):
    for j in range(n):

        if len(grid[i][j]) > 0:
            for k in range(len(grid[i][j]) -1, -1, -1):
                print(grid[i][j][k], end = ' ')
        else:
            print('None', end = '')
            
        print()