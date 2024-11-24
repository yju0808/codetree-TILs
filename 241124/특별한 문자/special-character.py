
s = input()

d = dict()

for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

ans = 'None'

for c in s:
    if d[c] == 1:
        ans = c
        break


print(ans)





