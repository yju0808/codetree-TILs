n = int(input())

bombs = [tuple(map(int, input().split())) for _ in range(n)]


bombs.sort(lambda x : (x[1], -x[0]))

time = 0
ans = 0

for p, t in bombs:

    if t >= time + 1:
        ans += p
        time = t + 1

print(ans)
