import sys

input = sys.stdin.readline
n, m = map(int, input().split())
smaller = dict()
for _ in range(m):
    a, b = map(int, input().split())
    if b in smaller:
        smaller[b].append(a)
    else:
        smaller[b] = [a]

visited = [0] * (n + 1)
result = []

def make_line(st):
    if visited[st]:
        return

    tmp = []
    if st in smaller:
        for el in smaller[st]:
            if visited[el]:
                continue
            tmp.extend(make_line(el))
    visited[st] = 1

    return tmp + [st]

for k, _ in smaller.items():
    tmp = make_line(k)
    if tmp:
        result.extend(tmp)

for i in range(1, n + 1):
    if not visited[i]:
        result.append(i)

print(' '.join(map(str, result)))