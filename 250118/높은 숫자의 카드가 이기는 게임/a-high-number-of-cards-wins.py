
n = int(input())

b_cards = [(int(input())) for _ in range(n)]

b_cards_set = set(b_cards)

a_cards = []

for i in range(1, 2 * n + 1):
    if i not in b_cards_set:
        a_cards.append(i)

ans = 0



a_cards.sort()
b_cards.sort()


b_index = 0

for i in range(len(a_cards)):

    if b_index < n and a_cards[i] > b_cards[b_index]:
        ans += 1
        b_index += 1


print(ans)