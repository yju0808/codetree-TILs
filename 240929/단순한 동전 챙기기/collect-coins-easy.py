from collections import deque

n = int(input())

grid = [input() for _ in range(n)]

coins = []
selected = []

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n


ans = float('inf')

def cal_dist(y1, x1, y2, x2):
    return abs(x2 - x1) + abs(y2 - y1)

def cal_ans():

    result = 0
    cur_y = s_y
    cur_x = s_x

    for num, y, x in selected:
        result += cal_dist(cur_y, cur_x, y, x)
        cur_y = y
        cur_x = x

    result += cal_dist(cur_y, cur_x, e_y, e_x)

    return result



def solve(last):

    global ans


    if len(selected) >= 3:
        ans = min(cal_ans(), ans)
        return

    for i in range(last, len(coins)):

        selected.append(coins[i])

        solve(i + 1)

        selected.pop()


    

s_y = 0
s_x = 0
e_y = 0
e_x = 0

num_count = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            s_y = i
            s_x = j

        if grid[i][j] == 'E':
            e_y = i
            e_x = j

        if '1' <= grid[i][j] <= '9':
            num_count += 1
            coins.append([grid[i][j], i, j])




if num_count < 3:
    print(-1)
else:
    coins.sort(key=lambda x: x[0])
    solve(0)
    print(ans)