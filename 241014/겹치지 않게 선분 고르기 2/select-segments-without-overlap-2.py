n = int(input())

lines = [tuple(map(int, input().split())) for _ in range(n)]

lines.sort(lambda x : x[1])

current_end = 0
count = 0

for x1, x2 in lines:
    if x1 > current_end:
        count += 1
        current_end = x2


print(count)