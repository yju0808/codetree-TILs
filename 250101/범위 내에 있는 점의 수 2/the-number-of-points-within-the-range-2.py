
n, q = map(int, input().split())

line = [0 for _ in range(100001)]
prefix_sum = [0 for _ in range(100001)]


points = list(map(int, input().split()))

for p in points:

    line[p] = 1

prefix_sum[0] = line[0]

for i in range(1, 100001):
    prefix_sum[i] = prefix_sum[i - 1] + line[i]


for _ in range(q):
    s, e = map(int, input().split())

    ans = prefix_sum[e] - prefix_sum[s] + line[s]
    print(ans)


