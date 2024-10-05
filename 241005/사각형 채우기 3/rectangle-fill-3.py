n = int(input())

dp = [0 for _ in range(n + 3)]

dp[0] = 1
dp[1] = 2
dp[2] = 7

def get_answer(n):

    if dp[n]:
        return dp[n]


    dp[n] = (get_answer(n - 1) * 2 + get_answer(n - 2) * 3 ) % 1000000000007

    for i in range(n - 3, -1, -1):
        dp[n] += get_answer(i) * 2

    return dp[n]


get_answer(n)
print(dp[n])