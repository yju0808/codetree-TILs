
n, k = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0 for _ in range(n)]

prefix_sum[0] = arr[0]

ans = 0

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]


for i in range(n):
    for j in range(i, n):
        temp = prefix_sum[j] - prefix_sum[i]  + arr[i]

        if temp == k:
            ans += 1


print(ans)

