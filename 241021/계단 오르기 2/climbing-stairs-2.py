n = int(input())
coins = list(map(int, input().split()))
coins.insert(0, 0)

dp = [[-1 for _ in range(4)] for _ in range(n + 1)]

dp[1][1] = coins[1]

def get_answer(n, count):
    if n <= 0:
        return 0

    if dp[n][count] != -1:
        return dp[n][count]

    one_step = 0
    two_step = 0

    if count < 3:
        one_step = get_answer(n - 1, count + 1) + coins[n]

    two_step = get_answer(n - 2, count) + coins[n]

    dp[n][count] = max(one_step, two_step)

    return dp[n][count]

result = get_answer(n, 0)
print(result)