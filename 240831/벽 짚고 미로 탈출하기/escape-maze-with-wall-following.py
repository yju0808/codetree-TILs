n = int(input())

y, x = map(int, input().split())

grid = [input() for _ in range(n)]

y -= 1
x -= 1


dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


direction = 0
time = 0

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n


ans = -1
visited = set()

while True:

    #print(y, x, direction)

    # 탈출인 경우
    if not is_valid_coord(y + dy[direction], x + dx[direction]):
        ans = time + 1
        break

    # 앞이 벽인 경우
    if grid[y + dy[direction]][x + dx[direction]] == '#':
        direction = (direction + 1) % 4

        if (y, x, direction) not in visited:
            visited.add((y, x, direction))
            continue
        else:
            break

    # 한칸 앞
    ny = y + dy[direction]
    nx = x + dx[direction]

    # 한칸 앞 오른쪽
    right_direction = direction - 1 if direction - 1 >= 0 else 3
    n_right_y = ny + dy[right_direction]
    n_right_x = nx + dx[right_direction]

    # 앞 오른쪽에 벽이 있는 경우
    if is_valid_coord(n_right_y, n_right_x) and grid[n_right_y][n_right_x] == '#':
        y = ny
        x = nx
        time += 1

        if (y, x, direction) not in visited:
            visited.add((y, x, direction))
        else:
            break
        

    # 앞 오른쪽에 벽이 없는 경우
    else:

        # 일단 앞으로 한 칸 이동 후 방향 전환
        y = ny
        x = nx
        direction = right_direction
        time += 1   

        if (y, x, direction) not in visited:
            visited.add((y, x, direction))
        else:
            break


        # 그 후 한칸 더 앞으로 이동
        y += dy[direction]
        x += dx[direction]
        time += 1

        if (y, x, direction) not in visited:
            visited.add((y, x, direction))
        else:
            break


print(ans)