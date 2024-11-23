MOD = 10**9 + 7
a = input()
n = len(a)

pt = [1] * (n + 1)
for i in range(1, n + 1):
    pt[i] = pt[i - 1] * 10 % MOD

dp = [[0] * 3 for _ in range(n + 1)]
ans = 0
is_369 = False
digit_sum = 0

for i in range(n):
    num = int(a[i])
    
    for x in range(10):
        if x in {3, 6, 9}:
            ans = (ans + sum(dp[i]) * pt[n-i-1]) % MOD
            continue
            
        for k in range(3):
            dp[i + 1][(x + k) % 3] = (dp[i + 1][(x + k) % 3] + dp[i][k]) % MOD
    
    for x in range(num):
        if is_369 or x in {3, 6, 9}:
            ans = (ans + pt[n-i-1]) % MOD
        else:
            dp[i + 1][(x + digit_sum) % 3] += 1
    
    if num in {3, 6, 9}:
        is_369 = True
    else:
        digit_sum += num

if is_369:
    ans = (ans + 1) % MOD
else:
    dp[n][digit_sum % 3] = (dp[n][digit_sum % 3] + 1) % MOD

ans = (ans + dp[n][0] - 1) % MOD
print(ans)