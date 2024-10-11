n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[None for _ in range(n)] for _ in range(n)]

dp[0][0] = ((grid[0][0], grid[0][0]))

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n

def get_answer(i, j):

    if dp[i][j]:
        return dp[i][j]


    current_num = grid[i][j]
    value = float('inf')

    final_min_num = current_num
    final_max_num = current_num

    if is_valid_coord(i - 1, j):
        temp_min_num, temp_max_num = get_answer(i - 1, j)

        temp_min_num = min(current_num, temp_min_num)
        temp_max_num = max(current_num, temp_max_num)

        temp_value = abs(temp_max_num - temp_min_num)

        if temp_value < value:
            final_min_num = temp_min_num
            final_max_num = temp_max_num
            value = abs(temp_max_num - temp_min_num)

    if is_valid_coord(i, j - 1):
        temp_min_num, temp_max_num = get_answer(i, j - 1)

        temp_min_num = min(current_num, temp_min_num)
        temp_max_num = max(current_num, temp_max_num)

        temp_value = abs(temp_max_num - temp_min_num)

        if temp_value < value:
            final_min_num = temp_min_num
            final_max_num = temp_max_num
            value = abs(temp_max_num - temp_min_num)


    dp[i][j] = (final_min_num, final_max_num)
    return dp[i][j]

min_num, max_num = get_answer(n - 1, n - 1)
print(abs(max_num - min_num))