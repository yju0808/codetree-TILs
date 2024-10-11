n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[None for _ in range(n)] for _ in range(n)]

dp[0][0] = [(grid[0][0], grid[0][0])]

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n

def get_answer(i, j):


    if dp[i][j]:
        return dp[i][j]

    current_num = grid[i][j]
    value = float('inf')

    final_min_num = current_num
    final_max_num = current_num

    result = []

    if is_valid_coord(i - 1, j):

        loop = get_answer(i - 1, j)

        for temp_min_num, temp_max_num in loop:
            temp_min_num = min(current_num, temp_min_num)
            temp_max_num = max(current_num, temp_max_num)

            temp_value = abs(temp_max_num - temp_min_num)

            if temp_value <= value:
                final_min_num = temp_min_num
                final_max_num = temp_max_num

                result.append((final_min_num, final_max_num))
                value = abs(temp_max_num - temp_min_num)

    if is_valid_coord(i, j - 1):
        loop = get_answer(i, j - 1)

        for temp_min_num, temp_max_num in loop:

            temp_min_num = min(current_num, temp_min_num)
            temp_max_num = max(current_num, temp_max_num)

            temp_value = abs(temp_max_num - temp_min_num)

            if temp_value <= value:
                final_min_num = temp_min_num
                final_max_num = temp_max_num

                result.append((final_min_num, final_max_num))
                value = abs(temp_max_num - temp_min_num)

    fianl_result = []

    for min_num, max_num in result:
        if abs(min_num - max_num) == value:
            fianl_result.append((min_num, max_num))


    dp[i][j] = fianl_result
    return dp[i][j]

ans = 0

get_answer(n - 1, n - 1)

for min_num, max_num in dp[n - 1][n - 1]:
    ans = abs(max_num - min_num)

print(ans)