a, b = map(int, input().split())
print(abs(a - b) - 1 if a != b else 0)
print(' '.join([str(i) for i in range(min(a, b) + 1, max(a, b))]))