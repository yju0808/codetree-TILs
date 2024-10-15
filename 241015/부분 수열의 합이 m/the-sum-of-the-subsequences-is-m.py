import sys

sys.setrecursionlimit(10**5)

n, m = map(int, input().split())

nums = list(map(int, input().split()))

dp = [[-1 for _ in range(m + 1)] for _ in range(n)]

def get_answer(index, k):

    if k == 0:
        return 0

    if index >= len(nums) or k < 0:
        return float('inf')

    if dp[index][k] != -1:
        return dp[index][k]

    temp = get_answer(index + 1, k)

    if k >= nums[index]:
        temp = min(temp, get_answer(index + 1, k - nums[index]) + 1)

    dp[index][k] = temp
    return dp[index][k]

ans = get_answer(0, m)

print(ans if ans != float('inf') else -1)