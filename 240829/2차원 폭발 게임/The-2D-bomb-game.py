n, m, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
temp_grid = [[0 for _ in range(n)] for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n


def simul_gravity(col):
    

    index = n - 1
    keep = 0

    for i in range(n - 1, -1, -1):

        if grid[i][col] == 0:
            continue

        if keep == 0:
            keep = grid[i][col]

        elif grid[i][col] != 0:
            grid[index][col] = keep
            keep = grid[i][col]
            index -= 1

    if keep != 0:
        grid[index][col] = keep

    for i in range(index - 1, -1, -1):
        grid[i][col] = 0

    

def simul_bomb(col):

    is_exploded = False


    overlap_count = 0
    before = grid[0][col]
    index = 0

    for i in range(n):

        if grid[i][col] == 0:
            continue

        if grid[i][col] == before:
            overlap_count += 1
            index = i

        else:
            if overlap_count >= m:
                for k in range(overlap_count):
                    grid[index - k][col] = 0
                    
                is_exploded = True

            overlap_count = 1

        before = grid[i][col]

    if overlap_count >= m:
        for k in range(overlap_count):
            grid[index - k][col] = 0
        
        is_exploded = True

    

    simul_gravity(col)

    return is_exploded



def simul_rotate():

    for i in range(n):
        for j in range(n):
            temp_grid[j][n - i - 1] = grid[i][j]

    for i in range(n):
        for j in range(n):
            grid[i][j] = temp_grid[i][j]

            
            
def simul():

    for i in range(n):
        while simul_bomb(i):
            pass

    simul_rotate()
    
    for i in range(n):
        simul_gravity(i)



for _ in range(k):
    simul()




for i in range(n):
    while simul_bomb(i):
        pass

    
result = 0

for i in range(n):
    for j in range(n):

        if grid[i][j] != 0:
            result += 1


print(result)