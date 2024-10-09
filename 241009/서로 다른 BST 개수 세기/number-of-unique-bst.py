n = int(input())

dp = [0 for _ in range(n +1)]

dp[0] = 1
dp[1] = 1

def get_answer(k):

    if dp[k]:
        return dp[k]

    ans = 0

    for i in range(0, n):
        ans += get_answer(i) * get_answer(n - i - 1)

    dp[n] = ans
    return dp[n]

print(get_answer(n))