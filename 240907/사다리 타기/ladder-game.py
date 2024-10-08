n, m = map(int, input().split())


lines = [tuple(map(int, input().split())) for _ in range(m)]
selected_lines = []


def simul(lines):

    li = [[0 for _ in range(15 + 1)] for _ in range(n + 1)]

    for line in lines:

        a, b = line
        li[a][b] = 1


    result = [0 for _ in range(n)]

    for i in range(1, n + 1):

        cur_n = i
        cur_h = 1

        for _ in range(15):

            if cur_n > n or cur_h > 15:
                continue

            if li[cur_n][cur_h]:
                cur_n += 1

            elif li[cur_n - 1][cur_h]:
                cur_n -= 1
            
            cur_h += 1

        result[i - 1] = cur_n

    return tuple(result)



result = simul(lines)
ans = float('inf')

def select(k):

    global ans

    if k >= len(lines):
        if simul(selected_lines) == result:
            ans = min(ans, len(selected_lines))
        return

    for i in range(len(lines)):
        line = lines[i]


        selected_lines.append(line)

        select(k + 1)

        selected_lines.pop()

        select(k + 1)


select(0)
    
print(ans)