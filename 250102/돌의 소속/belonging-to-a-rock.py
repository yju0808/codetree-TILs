
n, q = map(int, input().split())

group_1 = [0 for _ in range(n + 1)]
group_2 = [0 for _ in range(n + 1)]
group_3 = [0 for _ in range(n + 1)]

prefix_1 = [0 for _ in range(n + 1)]
prefix_2 = [0 for _ in range(n + 1)]
prefix_3 = [0 for _ in range(n + 1)]

groups = [group_1, group_2, group_3]
prefixes = [prefix_1, prefix_2, prefix_3]

for i in range(n):
    k = int(input())
    k -= 1
    groups[k][i] = 1

for i in range(3):
    prefixes[i][0] = groups[i][0]

for i in range(3):
    for j in range(1, n + 1):
        prefixes[i][j] = prefixes[i][j - 1] + groups[i][j]



for _ in range(q):
    
    a, b = map(int, input().split())

    a -= 1
    b -= 1

    for i in range(3):
        print(prefixes[i][b] - prefixes[i][a] + groups[i][a], end = ' ')

    print()


