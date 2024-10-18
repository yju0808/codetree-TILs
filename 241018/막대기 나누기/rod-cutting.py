n = int(input())

incomes =  list(map(int, input().split()))
incomes.insert(0, 0)

dp = [-float('inf') for _ in range(n +1)]
dp[0] = 0
dp[1] = incomes[1]

for i in range(1, n +1):
    for j in range(1, n + 1):

        if i >= j:
            dp[i] = max(dp[i], dp[i - j] +incomes[j])

print(dp[n] if dp[n] > 0 else -1)