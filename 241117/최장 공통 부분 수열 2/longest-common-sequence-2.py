

a = input()
b = input()

a = 'X' + a
b = 'X' + b

dp = [['' for _ in range(len(b))] for _ in range(len(a))]
dp[1][1] = a[0] if a[0] == b[0] else ''


def get_max_str(arr):

    max_len = len(arr[0])
    max_i = 0

    for i in range(1, len(arr)):
        if len(arr[i]) > max_len:
            max_len = len(arr[i])
            max_i = i


    return arr[i]


for i in range(1, len(a)):
    if a[i] == b[1]:
        dp[i][1] = a[i]
    else:
        dp[i][1] = dp[i - 1][1]


for i in range(1, len(b)):
    if a[1] == b[i]:
        dp[1][i] = b[i]
    else:
        dp[1][i] = dp[1][i - 1]

for i in range(2, len(a)):
    for j in range(2, len(b)):

        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + a[i]

        else:
            dp[i][j] = get_max_str([dp[i - 1][j], dp[i][j - 1]])


ans = dp[len(a) - 1][len(b) - 1]

print(ans)