
n = int(input())

meetings = [tuple(map(int, input().split())) for _ in range(n)]

meetings.sort(lambda x: x[1])


count = 0
current = 0

for s, e in meetings:
    if s >= current:
        count += 1
        current = e

print(count)


