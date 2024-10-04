n = int(input())


dp = [0 for _ in range(n + 3)]
dp[2] = 1
dp[3] = 1 

def get_answer(n):

    if n < 2:
        return 0

    if dp[n]:
        return dp[n]


    dp[n] = (get_answer(n - 2) + get_answer(n - 3)) % 10007
    return dp[n]



get_answer(n)
print(dp[n] % 10007)