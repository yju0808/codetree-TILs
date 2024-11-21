
n = int(input())

d = dict()

for i in range(n):
    word = input()

    if word in d:
        d[word] += 1
    else:
        d[word] = 1




max_value = 0


for key, value in d.items():

    if value > max_value:
        max_value = value

print(max_value)






