n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

AB_sum = {}
for a in A:
    for b in B:
        total = a + b
        if total in AB_sum:
            AB_sum[total] += 1
        else:
            AB_sum[total] = 1

count = 0
for c in C:
    for d in D:
        target = -(c + d)
        if target in AB_sum:
            count += AB_sum[target]

print(count)
