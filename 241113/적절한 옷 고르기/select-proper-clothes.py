
n, m = map(int, input().split())

clothes = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[-float('inf') for _ in range(n)] for _ in range(m + 1)]

for i in range(0, n):

    cs, ce, cv = clothes[i]

    for j in range(0, n):

        bs, be, bv = clothes[j]

        if not ((cs <= 2 <= ce) or (bs <= 1 <= be)):
            continue

        dp[2][i] = max(dp[2][i], abs(bv - cv))


    s, e, v = clothes[i]
    dp[0][i] = 0

for i in range(3, m +1):

    for j in range(0, n):

        cs, ce, cv = clothes[j]

        for k in range(0, n):

            bs, be, bv = clothes[k]

            if not ((cs <= i <= ce) or (bs <= i - 1 <= be)):
                continue

            dp[i][j] = max(dp[i][j], dp[i - 1][k] + abs(bv - cv))


ans = 0

for i in range(0, n):
    ans = max(dp[m][i], ans)


print(ans)

        

        