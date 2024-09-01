from collections import deque

n, m, k = map(int, input().split())


def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n


dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

direction_mapper = {'U':1, 'D':3, 'R':0, 'L':2}

snake = deque()
apple = set()

snake.append((0, 0))
time = 0

for _ in range(m):
    y, x = map(int, input().split())
    
    y -= 1
    x -= 1

    apple.add((y, x))


time = 0
is_ended = False


for _ in range(k):

    d, p = input().split()
    d = direction_mapper[d]
    p = int(p)

    for i in range(p):

        y, x = snake[-1]

        ny = y + dy[d]
        nx = x + dx[d]

        if not is_valid_coord(ny, nx) or (ny, nx) in snake:
            is_ended = True
            time += 1
            break

        if (ny, nx) in apple:
            snake.append((ny, nx))
            apple.remove((ny, nx))

        else:
            snake.popleft()
            snake.append((ny, nx))
            
        time += 1

    if is_ended:
        break


print(time)