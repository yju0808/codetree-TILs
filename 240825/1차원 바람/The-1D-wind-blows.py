n, m, q = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]


def shift(r, d):


    if d == 'L':
        temp = grid[r][m - 1]
        for i in range(m - 1, 0, -1):
            grid[r][i] = grid[r][i - 1]

        grid[r][0] = temp 

    else:
        temp = grid[r][0]
        for i in range(0, m - 1):
            grid[r][i] = grid[r][i + 1]

        grid[r][m - 1] = temp
    

def is_valid_row(r):
    return 0 <= r < n

def check(current_row, target_row):

    if not is_valid_row(current_row) or not is_valid_row(target_row):
        return False
    
    for i in range(m):
        if grid[current_row][i] == grid[target_row][i]:
            return True
    
    return False



for _ in range(q):
    r, d = input().split()
    r = int(r)
    r -= 1

    reverse_map = {'R':'L', 'L':'R'}


    shift(r, d)
    up_d = d
    down_d = d

    for i in range(r, 0, -1):
        if (check(i, r - 1)):
            up_d = reverse_map[up_d]
            shift(r - 1, up_d)
        else:
            break

    for i in range(r, n - 1):
        if (check(r, r + 1)):
            print(r)
            down_d = reverse_map[down_d]
            shift(r + 1, down_d)
        else:
            break



for row in grid:
    print(*row)