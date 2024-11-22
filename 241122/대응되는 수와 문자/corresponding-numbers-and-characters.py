
num_dict = dict()
word_dict =  dict()

n, m = map(int, input().split())

for i in range(1, n + 1):
    
    word = input()
    word_dict[word] = i
    num_dict[i] = word

for _ in range(m):
    
    q = input()

    if q.isdigit():
        print(num_dict[int(q)])
    else:
        print(word_dict[q])