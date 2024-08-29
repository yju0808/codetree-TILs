n, m, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]


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

def check_should_explo():
    for j in range(n):

        overlap_count = 1
        before = None

        for i in range(n):

            if grid[i][j] == 0:
                continue

            if grid[i][j] == before:
                overlap_count += 1

            else:
                if overlap_count >= m:
                    return True

            before = grid[i][j]
        
        if overlap_count >= m:
            return True

    return False



def simul_bomb():


    for j in range(n):

        overlap_count = 1
        before = None
        index = 0

        for i in range(n):

            if grid[i][j] == 0:
                continue

            if grid[i][j] == before:
                overlap_count += 1
                index = i

            else:
                if overlap_count >= m:
                    for k in range(overlap_count):
                        grid[index - k][j] = 0
                        
                    overlap_count = 0

            before = grid[i][j]
        
        if overlap_count >= m:
            for k in range(overlap_count):
                grid[index - k][j] = 0



def simul_rotate():

    temp_grid = [[0 for _ in range(n)] for _ in range(n)]

    
    for i in range(n):
        for j in range(n):
            temp_grid[j][n - i - 1] = grid[i][j]

    for i in range(n):
        for j in range(n):
            grid[i][j] = temp_grid[i][j]

            


            
def simul():

    simul_bomb()
    simul_gravity()
    simul_rotate()
    simul_gravity()





for _ in range(k):
    simul()



while check_should_explo():
    simul_bomb()
    simul_gravity()

    
result = 0

for i in range(n):
    for j in range(n):

        if grid[i][j] != 0:
            result += 1


print(result)