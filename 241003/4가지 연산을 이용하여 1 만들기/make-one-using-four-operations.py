from collections import deque

n = int(input())







visited = set()
dq = deque()
dq.append((n, 0))
visited.add(n)

ans = -1

while dq:

    num, count = dq.popleft()

    if num == 1:
        ans = count
        break


    if num - 1 not in visited:
        dq.append((num - 1, count + 1))
        visited.add(num - 1)

    if num + 1 not in visited:
        dq.append((num + 1, count + 1))
        visited.add(num + 1)
    
    if num % 2 == 0 and num // 2 not in visited:
        dq.append((num // 2, count + 1))
        visited.add(num // 2)

    if num % 3 == 0 and num // 3 not in visited:
        dq.append((num // 3, count + 1))
        visited.add(num // 3)

    

print(ans)