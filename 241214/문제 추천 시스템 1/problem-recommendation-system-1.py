
from sortedcontainers import SortedSet

s = SortedSet()


n = int(input())

for _ in range(n):
    p, l = map(int, input().split())

    s.add((l, p))


m = int(input())

for _ in range(m):

    inputs = input().split()

    command = inputs[0]

    if command == 'rc':
        
        pam = int(inputs[1])

        if pam == 1:
            print(s[-1][1])
        else:
            print(s[0][1])


    elif command == 'sv':
        p, l = int(inputs[1]), int(inputs[2])

        index = s.bisect_left((l, p))

        s.remove(s[index])



    elif command == 'ad':
        p, l = int(inputs[1]), int(inputs[2])

        s.add((l, p))