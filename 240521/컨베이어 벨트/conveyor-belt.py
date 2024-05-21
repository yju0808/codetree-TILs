n, t = map(int, input().split())

up = list(map(int, input().split()))
down = list(map(int, input().split()))

down = list(reversed(down))

for i in range(t):

    temp1 = up[n - 1]
    temp2 = down[0]

    for j in range(0, n - 1):
        up[n - j - 1] = up[n - j - 2]
        down[j] = down[j + 1]

    down[n - 1] = temp1
    up[0] = temp2

print(*up)
print(*reversed(down))