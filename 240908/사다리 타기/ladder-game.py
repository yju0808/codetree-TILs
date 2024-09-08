n, m = map(int, input().split())


lines = [tuple(map(int, input().split())) for _ in range(m)]
selected_lines = []
lines.sort(lambda x : x[1])

def simul(lines):
    
    origin = [i for i in range(n)]


    for a, b in lines:

        a -= 1
        origin[a], origin[a + 1] = origin[a + 1], origin[a]


    return tuple(origin)



result = simul(lines)


ans = m

def select(k):

    global ans

    if k >= len(lines):
        if simul(selected_lines) == result:
            ans = min(ans, len(selected_lines))
        return

    
    line = lines[k]

    selected_lines.append(line)

    select(k + 1)

    selected_lines.pop()

    select(k + 1)



select(0)
    
print(ans)