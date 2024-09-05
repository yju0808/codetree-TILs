dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

direction_mapper = {'U':1,'D':3,'R':0,'L':2}

def is_valid_coord(y, x):
    return -2000 <= y <= 2000 and -2000 <= x <= 2000


beads = {}
temp_beads = {}

t = int(input())


for _ in range(t):

    n = int(input())

    for i in range(n):

        x, y, w, d = input().split()

        y = int(y)
        x = int(x)
        w = int(w)

        y *= 2
        x *= 2


        beads[(y,x)] = [(direction_mapper[d], w, i + 1)]

    ans = -1



    for time in range(4000):


        for y, x in beads.keys():

            for d, w, i in beads[(y, x)]:

                ny = y
                nx = x
                nd = d

                if not is_valid_coord(ny + dy[nd], nx + dx[nd]):
                    nd = (nd + 2) % 4

                ny += dy[nd]
                nx += dx[nd]

                if (ny, nx) in temp_beads:
                    temp_beads[(ny, nx)].append((nd, w, i))

                else:
                    temp_beads[(ny, nx)] = [(nd, w, i)]


        
        for y, x in temp_beads.keys():
            if len(temp_beads[(y, x)]) > 1:

                temp_beads[(y, x)].sort(lambda x: (-x[1], -x[2]))
                rest = temp_beads[(y, x)][0]
                temp_beads[(y, x)] = [rest]

                ans = time + 1
        
        beads = temp_beads
        temp_beads = {}

    print(ans)