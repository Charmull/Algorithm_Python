# 사이클 생기는지 확인
# a, b가 같은 그룹인지 확인 - union-find
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
game = [list(map(int, input().split())) for _ in range(m)]
root = [i for i in range(n)]
result = 0

def find_root(e):
    while root[e] != e:
        e = root[e]
    return e

for i in range(m):
    a, b = game[i]
    a_root = find_root(a)
    b_root = find_root(b)
    if a_root == b_root:
        result = i + 1
        break

    if a_root < b_root:
        root[b_root] = a_root
    elif a_root > b_root:
        root[a_root] = b_root

print(result)