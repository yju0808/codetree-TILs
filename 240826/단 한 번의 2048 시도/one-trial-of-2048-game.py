input_grid = [list(map(int, input().split())) for _ in range(4)]

grid = [[] for _ in range(4)]

dir_ = input()

result_grid = [[0 for _ in range(4)] for _ in range(4)]


for i in range(4):
    for j in range(4):
        if input_grid[i][j] != 0:
            grid[i].append(input_grid[i][j])

    while len(grid[i]) < 4:
        grid[i].append(0)



if dir_ == 'L':

    for i in range(4):

        index = 0
        temp = grid[i][0]

        for j in range(1, 4):

            if grid[i][j] == 0:
                break

            if temp == None:
                result_grid[i][index] = grid[i][j]
                continue


            if grid[i][j] == temp:
                result_grid[i][index] = temp * 2
                index += 1
                temp = None
                

            elif grid[i][j] != temp:
                result_grid[i][index] = temp
                temp = grid[i][j]
                index += 1

        if temp != None:
            result_grid[i][index] = temp


elif dir_ == 'R':
    
    for i in range(3, -1, -1):

        index = 3
        temp = grid[i][3]


        for j in range(2, -1, -1):

            if grid[i][j] == '0':
                continue


            if grid[i][j] == temp:
                result_grid[i][index] = temp * 2
                index -= 1

            else:
                temp = grid[i][j]



elif dir_ == 'U':

    for j in range(0, 4):

        index = 0
        temp = grid[0][j]


        for i in range(1, 4):

            if grid[i][j] == '0':
                continue


            if grid[i][j] == temp:
                result_grid[i][index] = temp * 2
                index += 1

            else:
                temp = grid[i][j]

else:
    for j in range(0, 4):

        index = 0
        temp = grid[0][j]


        for i in range(1, 4):

            if grid[i][j] == '0':
                continue


            if grid[i][j] == temp:
                result_grid[i][index] = temp * 2
                index += 1

            else:
                temp = grid[i][j]


for row in result_grid:
    print(*row)