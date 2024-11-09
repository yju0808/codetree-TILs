n = int(input())

cards = [tuple(map(int, input().split())) for _ in range(2 * n)]

cards.sort(lambda x:  x[0]-x[1])

ans = 0

for i in range(0, n):
    ans += cards[i][1]

for i in range(n, 2 * n):
    ans += cards[i][0]

print(ans)