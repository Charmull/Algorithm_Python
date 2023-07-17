import math

n, k = map(int, input().split())
students = [[0, 0] for _ in range(6)]
for _ in range(n):
    s, y = map(int, input().split())
    students[y - 1][0 if s == 0 else 1] += 1
total = 0
for grade in students:
    total += math.ceil(grade[0] / k) + math.ceil(grade[1] / k)
print(total)