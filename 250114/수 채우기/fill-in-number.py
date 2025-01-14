

n = int(input())

count = 0
current_n = n

for i in range(n):

    if current_n == 0:
        break

    if current_n % 5 == 0:
        count += current_n // 5
        break

    else:
        count += 1
        current_n -= 2

print(count)