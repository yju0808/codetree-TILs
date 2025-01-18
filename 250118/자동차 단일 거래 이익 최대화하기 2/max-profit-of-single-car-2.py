n = int(input())

nums = list(map(int, input().split()))

current = nums[0]
ans = 0

for i in range(1, n):

    ans = max(ans, nums[i] - current)

    current = min(nums[i], current)

print(ans)

