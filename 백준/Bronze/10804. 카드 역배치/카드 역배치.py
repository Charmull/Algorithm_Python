cards = [i for i in range(1, 21)]
for _ in range(10):
    start, end = map(int, input().split())
    cards[start - 1:end] = cards[start - 1:end][::-1]
print(' '.join(map(str, cards)))