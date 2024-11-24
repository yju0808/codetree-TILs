
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
    for j in range(i + 1, len(nums)):

        n1 = nums[i]
        n2 = nums[j]

        target = k - (n1 + n2)

        if target in d:

            count = d[target]

            if target == n1:
                count -= 1
            
            if target == n2:
                count -= 1

            if count > 0:
                ans += count
                d[n1] -= 1
                d[n2] -= 1
                


print(ans)
