import sys

input = sys.stdin.readline
n = int(input())
result = 0

def chk(word):
    s = set(word[0])
    prev = word[0]
    for w in word[1:]:
        if prev == w:
            continue
        if w in s:
            return 0
        s.add(w)
        prev = w
    return 1

for _ in range(n):
    word = input().strip()
    result += chk(word)
print(result)