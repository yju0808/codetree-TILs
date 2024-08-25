n, m = map(int, input().split())

bombs_a = [int(input()) for _ in range(n)]

bombs_b = []


while bombs_a:

    is_ended = True
    count = 0
    temp = bombs_a[0]

    while bombs_a:
        
        current = bombs_a.pop()

        if current != temp:

            if count >= m and bombs_b:
                for i in range(count):
                    bombs_b.pop()
                is_ended = False


            count = 1
            bombs_b.append(current)
            temp = current
                
        else:
            bombs_b.append(current)
            count += 1
            


    
    if count >= m and bombs_b:
        for i in range(count):
                bombs_b.pop()

        is_ended = False

    while bombs_b:
        bombs_a.append(bombs_b.pop())

    if is_ended:
        break


print(len(bombs_a))
for bomb in bombs_a:
    print(bomb)