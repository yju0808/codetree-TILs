
n, k = map(int, input().split())
arr = [[0 for _ in range(n + 1)]]
prefix_sum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n):
    arr.append([0] + list(map(int, input().split())))


ans = 0
k -= 1

def is_valid_coord(y, x):
    return 0 <= y < n + 1 and 0 <= x < n + 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + arr[i][j] 




for i in range(1, n + 1):
    for j in range(1, n + 1):

        i2, j2 = i + k, j + k

        if not is_valid_coord(i2, j2):
            continue

        p_sum = prefix_sum[i2][j2] - prefix_sum[i2][j - 1] - prefix_sum[i - 1][j2] + prefix_sum[i - 1][j - 1]
        ans = max(ans, p_sum)


print(ans)

