
n = int(input())

words = [input() for _ in range(n)]

ans_dict = dict()


for word in words:


    sortedWord = ''.join(sorted(word))

    if sortedWord in ans_dict:
        ans_dict[sortedWord] += 1
    else:
        ans_dict[sortedWord] = 1



ans = 0

for key, value in ans_dict.items():
    if value > ans:
        ans = value

print(ans)

