n = int(input())


dp = [0 for _ in range(n + 3)]
dp[2] = 1
dp[3] = 1 

def get_answer(n):

    if dp[n]:
        return dp[n]


    dp[n] = dp[n - 2] + dp[n - 3]
    return dp[n]



get_answer(n)
print(dp[n])