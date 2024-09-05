dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

direction_mapper = {'U':1,'D':3,'R':0,'L':2}

def is_valid_coord(y, x):
    return 0 <= y <= 4000 and 0 <= x <= 4000




t = int(input())


for _ in range(t):

    beads = []
    temp_beads = []
    beads_index = [[-1 for _ in range(4000 + 1)] for _ in range(4000 + 1)]

    n = int(input())

    for i in range(n):

        x, y, w, d = input().split()

        y = int(y)
        x = int(x)
        w = int(w)

        y *= 2
        x *= 2

        y += 2000
        x += 2000

        beads.append((y, x, direction_mapper[d], w, i + 1))

    ans = -1

    for time in range(4000):
  

        for y, x, d, w, i in beads:

            ny = y
            nx = x
            nd = d

            ny += dy[nd]
            nx += dx[nd]

            if not is_valid_coord(ny, nx):
                continue

            if beads_index[ny][nx] == -1:
                temp_beads.append((ny, nx, nd, w, i))
                beads_index[ny][nx] = len(temp_beads) - 1
            else:   

                index = beads_index[ny][nx]

                # 1이 현재, 2는 과거 기록된 것
                w1 = w
                w2 = temp_beads[index][3]

                index1 = i
                index2 = temp_beads[index][4]

                # 현재것이 더 크면 교체
                if w1 > w2 or (w1 == w2 and index1 > index2):
                    temp_beads[index] = (ny, nx, nd, w, i)
                
                ans = time + 1
                    

        for y, x, d, w, i in temp_beads:
            beads_index[y][x] = -1

        beads = temp_beads
        temp_beads = []


    print(ans)