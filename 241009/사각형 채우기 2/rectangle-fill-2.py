n = int(input())

dp = [0 for _ in range(n +1)]

dp[0] = 1
dp[1] = 1

def get_answer(k):

    if dp[k]:
        return dp[k]

    dp[k] = get_answer(k - 1) + get_answer(k - 2) *2
    return dp[k]

print(get_answer(n))