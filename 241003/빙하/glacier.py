from collections import deque

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]




dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

visited = [[False for _ in range(m)] for _ in range(n)]

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < m






ans_time = 0
time_for_size = dict()


dq = deque()
dq.append((0, 0, 0))
temp_dq = deque()


while dq:

    for y, x, time in dq:
        grid[y][x] = 0


        if time in time_for_size:
            time_for_size[time] += 1
        else:
            time_for_size[time] = 1



    while dq:
        temp_dq.append(dq.popleft())

    while temp_dq:

        y, x, time = temp_dq.popleft()
        ans_time = max(time, ans_time)
            

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if is_valid_coord(ny, nx) and not visited[ny][nx] and grid[y][x] != 1:

                if grid[ny][nx] == 1:
                    dq.append((ny, nx, time + 1))

                else:
                    temp_dq.append((ny, nx, time))

                visited[ny][nx] = True

print(ans_time, time_for_size[ans_time])