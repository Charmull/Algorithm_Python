import sys

input = sys.stdin.readline
n, s = map(int, input().split())
l = list(map(int, input().split()))
log = []
appended = [0] * n
result = 0

def make_s(k):
    global result

    if log and sum(log) == s:
        result += 1
    
    for i in range(k, n):
        if appended[i]:
            continue
        log.append(l[i])
        appended[i] = 1
        make_s(i + 1)
        log.pop()
        appended[i] -= 1

make_s(0)
print(result)