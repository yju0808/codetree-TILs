
n = int(input())

nums = list(map(int, input().split()))

nums.sort()

current = nums[0]
ans = 0

for i in range(1, len(nums)):
    current += nums[i]
    ans += current

print(ans)