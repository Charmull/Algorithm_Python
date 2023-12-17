import sys

word = sys.stdin.readline().strip()
candidate = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        candidate.append(a[::-1] + b[::-1] + c[::-1])

candidate.sort()
print(candidate[0])