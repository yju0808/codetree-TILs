k, n = map(int, input().split())

result = []

def choose(t):

    if t == n + 1:
        print(" ".join(result))
        return

    for i in range(1, k + 1):
        result.append(str(i))
        choose(t + 1)
        result.pop()

choose(1)