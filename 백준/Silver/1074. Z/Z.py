import sys

input = sys.stdin.readline
n, r, c = map(int, input().split())

def find_num(k, r, c):
    if k == 1:
        if r == 0 and c == 0:
            return 0
        elif r == 0 and c == 1:
            return 1
        elif r == 1 and c == 0:
            return 2
        elif r == 1 and c == 1:
            return 3
    
    half_line = 2 ** k // 2
    if r < half_line and c < half_line:
        return find_num(k - 1, r, c)
    elif r < half_line and c >= half_line:
        return half_line ** 2 + find_num(k - 1, r, c - half_line)
    elif r >= half_line and c < half_line:
        return half_line ** 2 * 2 + find_num(k - 1, r - half_line, c)
    elif r >= half_line and c >= half_line:
        return half_line ** 2 * 3 + find_num(k - 1, r - half_line, c - half_line)

print(find_num(n, r, c))