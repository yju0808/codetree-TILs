import copy

a, b = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.insert(0, 0)
b.insert(0, 0)

dp = [[[] for _ in range(len(b))] for _ in range(len(a))]
dp[1][1] = [a[1]] if a[1] == b[1] else []


def get_max_str(arr1, arr2):

    if len(arr1) > len(arr2):
        return copy.deepcopy(arr1)
    elif len(arr1) < len(arr2):
        return copy.deepcopy(arr2)


    return copy.deepcopy(arr1) if arr1 < arr2  else copy.deepcopy(arr2)


for i in range(1, len(a)):
    if a[i] == b[1]:
        dp[i][1] = [a[i]]
    else:
        dp[i][1] = copy.deepcopy(dp[i - 1][1])


for i in range(1, len(b)):
    if a[1] == b[i]:
        dp[1][i] = [b[i]]
    else:
        dp[1][i] = copy.deepcopy(dp[1][i - 1])

for i in range(2, len(a)):
    for j in range(2, len(b)):

        if a[i] == b[j]:
            dp[i][j] = copy.deepcopy(dp[i - 1][j - 1]) + [a[i]]

        else:
            dp[i][j] = get_max_str(dp[i - 1][j], dp[i][j - 1])


ans = dp[len(a) - 1][len(b) - 1]

print(*ans)