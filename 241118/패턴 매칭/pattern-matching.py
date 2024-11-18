
s = input()
p = input()


dp = [[False for _ in range(len(p))] for _ in range(len(s))]
dp[0][0] = True

for i in range(len(s)):
    for j in range(len(p)):

        if p[j] == '*':
            dp[i][j] = dp[i - 1][j - 1]

        elif p[j] == '.':
            dp[i][j] = True

        else:
            if s[i] == p[j]:
                dp[i][j] = True




    
print('true' if dp[len(s) - 1][len(p) - 1] else 'false')

