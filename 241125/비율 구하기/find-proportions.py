from sortedcontainers import SortedDict

sd = SortedDict()  

n = int(input())

for _ in range(n):

    word = input()

    if word in sd:
        sd[word] += 1
    else:
        sd[word] = 1


for key, value in sd.items():

    print(f'{key} {((value / n) * 100):.4f}')