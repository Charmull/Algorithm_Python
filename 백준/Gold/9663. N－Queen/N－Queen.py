import sys

input = sys.stdin.readline
n = int(input())

is_used1 = [False] * n
is_used2 = [False] * (2 * n - 1)
is_used3 = [False] * (2 * n - 1)
result = 0

def n_queen(row):
    global result

    if row == n:
        result += 1
        return 0
    
    for i in range(n):
        if is_used1[i] or is_used2[i + row] or is_used3[row - i + n - 1]:
            continue
        is_used1[i] = True
        is_used2[i + row] = True
        is_used3[row - i + n - 1] = True
        n_queen(row + 1)
        is_used1[i] = False
        is_used2[i + row] = False
        is_used3[row - i + n - 1] = False

n_queen(0)
print(result)