n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]


def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n


def get_answer(y, x):

    if dp[y][x]:
        return dp[y][x]

    ans = float('inf')
    current_num = grid[y][x]

    if is_valid_coord(y - 1, x):
        ans = min(ans, get_answer(y - 1, x))

    if is_valid_coord(y, x - 1):
        ans = min(ans, get_answer(y, x - 1))

    ans = max(ans, current_num)

    dp[y][x] = ans
    return dp[y][x]

final_ans = float('inf')

for min_num in range(1, 101):

    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if grid[i][j] < min_num:
                grid[i][j] = float('inf')

    dp[0][0] = grid[0][0]

    
    ans = get_answer(n - 1, n - 1)
    if ans == float('inf'):
        continue

    final_ans = min(final_ans, abs(ans - min_num))

print(final_ans)