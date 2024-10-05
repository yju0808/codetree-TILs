n = int(input())

dp = [0 for _ in range(n + 3)]

dp[1] = 2
dp[2] = 7

def get_answer(n):

    if dp[n]:
        return dp[n]


    dp[n] = (get_answer(n - 1) * 2 + get_answer(n - 2) * 3 + 2) % 1000000000007

    return dp[n]


get_answer(n)
print(dp[n])