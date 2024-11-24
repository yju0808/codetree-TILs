
n, k = map(int, input().split())

nums = list(map(int, input().split()))

d = dict()
ans = 0


for n in nums:
    if n in d:
        d[n] += 1
    else:
        d[n] = 1

for i in range(len(nums)):

    d[nums[i]] -= 1

    for j in range(i):

        target = k - (nums[i] + nums[j])

        if target in d:
            ans += d[target]
                


print(ans)
