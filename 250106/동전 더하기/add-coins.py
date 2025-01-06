n, k = map(int, input().split())

coins = []

for _ in range(n):

    coin = int(input())

    coins.append(coin)

count = 0
for i in range(len(coins) - 1, -1, -1):
    count += k // coins[i]
    k = k % coins[i]

print(count)

