n = int(input())
MAX = 200002
line = [0 for _ in range(MAX)]

for _ in range(n):
    x1, x2 = map(int, input().split())
    line[x1] += 1
    line[x2] -= 1

ans = 0
current = 0
for i in range(1, MAX):
    
    ne = current + line[i]

    if ne > current:
        ans = ne

    current = ne
    

print(ans)

