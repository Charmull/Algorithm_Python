import sys

input = sys.stdin.readline
n = int(input())
result = [[0] * n for _ in range(n)]

def make_pattern(start_row, start_col, k):
    if k == 1:
        result[start_row][start_col] = "*"
        return 0
    
    for row in (start_row, start_row + k // 3, start_row + k // 3 * 2):
        for col in (start_col, start_col + k // 3, start_col + k // 3 * 2):
            if row == start_row + k // 3 and col == start_col + k // 3:
                for i in range(k // 3):
                    for j in range(k // 3):
                        result[row + i][col + j] = " "
                continue
            make_pattern(row, col, k // 3)
        

make_pattern(0, 0, n)
for v in result:
    print(''.join(v))