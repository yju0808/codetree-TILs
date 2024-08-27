grid = [list(map(int, input().split())) for _ in range(4)]

dir_ = input()

result_grid = [[0 for _ in range(4)] for _ in range(4)]



if dir_ == 'L':

    for i in range(4):

        keep = 0
        index = 0
        start_index = 0

        for j in range(0, 4):
            if grid[i][j] != 0:
                keep = grid[i][j]
                start_index = j + 1
                break

        for j in range(start_index, 4):

            current = grid[i][j]

            if current == 0:
                continue

            if keep == 0:
                keep = grid[i][j]

            elif current == keep:
                result_grid[i][index] = current + keep
                index += 1
                keep = 0
            
            else:
                result_grid[i][index] = keep
                keep = current
                index += 1


        if keep != 0:
            result_grid[i][index] = keep



elif dir_ == 'R':
    
    for i in range(4):

        keep = 3
        index = 3
        start_index = 3

        for j in range(3, -1, -1):
            if grid[i][j] != 0:
                keep = grid[i][j]
                start_index = j - 1
                break

        for j in range(start_index, -1, -1):

            current = grid[i][j]

            if current == 0:
                continue

            if keep == 0:
                keep = grid[i][j]

            elif current == keep:
                result_grid[i][index] = current + keep
                index -= 1
                keep = 0
            
            else:
                result_grid[i][index] = keep
                keep = current
                index -= 1


        if keep != 0:
            result_grid[i][index] = keep



elif dir_ == 'U':
    for j in range(4):

        keep = 0
        index = 0
        start_index = 0

        for i in range(0, 4):
            if grid[i][j] != 0:
                keep = grid[i][j]
                start_index = i + 1
                break

        for i in range(start_index, 4):

            current = grid[i][j]

            if current == 0:
                continue

            if keep == 0:
                keep = grid[i][j]

            elif current == keep:
                result_grid[i][index] = current + keep
                index += 1
                keep = 0
            
            else:
                result_grid[i][index] = keep
                keep = current
                index += 1


        if keep != 0:
            result_grid[i][index] = keep

else:
    for j in range(4):

        keep = 3
        index = 3
        start_index = 3

        for i in range(3, -1, -1):
            if grid[i][j] != 0:
                keep = grid[i][j]
                start_index = i - 1
                break

        for i in range(start_index, -1, -1):

            current = grid[i][j]

            if current == 0:
                continue

            if keep == 0:
                keep = grid[i][j]

            elif current == keep:
                result_grid[i][index] = current + keep
                index -= 1
                keep = 0
            
            else:
                result_grid[i][index] = keep
                keep = current
                index -= 1


        if keep != 0:
            result_grid[i][index] = keep


for row in result_grid:
    print(*row)