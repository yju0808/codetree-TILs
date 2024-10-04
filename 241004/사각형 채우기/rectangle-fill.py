n = int(input())


dp = [0 for _ in range(n + 1)]

dp[1] = 1
dp[2] = 2

def get_answer(n):

    if dp[n]:
        return dp[n]


    dp[n] = (get_answer(n - 1) + get_answer(n - 2)) % 10007
    return dp[n]


get_answer(n)
print(dp[n])