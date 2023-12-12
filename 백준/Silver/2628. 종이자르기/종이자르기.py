import sys

input = sys.stdin.readline
m, n = map(int, input().split())
rows = [0] * n
cols = [0] * m
for _ in range(int(input())):
    w, num = map(int, input().split())
    if w == 0:
        rows[num] = 1
    else:
        cols[num] = 1

row_cut = []
prev = 0
for i in range(n):
    if rows[i]:
        row_cut.append(i - prev)
        prev = i
    if i == n - 1:
        row_cut.append(n - prev)
col_cut = []
prev = 0
for i in range(m):
    if cols[i]:
        col_cut.append(i - prev)
        prev = i
    if i == m - 1:
        col_cut.append(m - prev)

print(max(row_cut) * max(col_cut))