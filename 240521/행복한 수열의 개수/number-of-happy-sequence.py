n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

happy_count = 0

for i in range(n):

    before = None
    continuous_count = 0

    for num in board[i]:

        if num != before:
            continuous_count = 1
        else:
            continuous_count += 1

        if continuous_count == m:
            happy_count += 1
            break

        before = num

    before = None
    continuous_count = 0

    for j in range(n):

        if board[j][i] != before:
            continuous_count = 1
        else:
            continuous_count += 1

        if continuous_count == m:
            happy_count += 1
            break

        before = board[j][i]

        
print(happy_count)