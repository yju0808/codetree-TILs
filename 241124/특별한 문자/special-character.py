s = input()

d = dict()

ans = 'None'

for c in s:
    if c not in d:
        ans = c
        d[c] = 1
    else:
        d[c] += 1
        if ans == c:
            ans = 'None'

            for key, value in d.items():
                if value == 1:
                    ans = key

print(ans)