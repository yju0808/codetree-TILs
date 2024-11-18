
s = ' ' + input()
p = ' ' + input()


dp = [[False for _ in range(len(p))] for _ in range(len(s))]
dp[0][0] = True  


for j in range(1, len(p)):
    if p[j] == '*' and j >= 2:
        dp[0][j] = dp[0][j - 2]


for i in range(1, len(s)):
    for j in range(1, len(p)):
        
        if p[j] == '*':
            dp[i][j] = dp[i][j - 2]

            if p[j - 1] == '.' or p[j - 1] == s[i]:
                dp[i][j] = dp[i][j] or dp[i - 1][j]

        elif p[j] == '.' or p[j] == s[i]:
            dp[i][j] = dp[i - 1][j - 1]



ans = 'false'
if dp[len(s) - 1][len(p) - 1]:
    ans = 'true'


print(ans)
