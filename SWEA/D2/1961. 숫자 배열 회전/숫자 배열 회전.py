T = int(input())

def rotate(board, n):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = board[n - 1 - j][i]
    return result

for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    result90 = rotate(board, n)
    result180 = rotate(result90, n)
    result270 = rotate(result180, n)

    print('#', test_case, sep='')
    for i in range(n):
        print(''.join(map(str, result90[i])), end=' ')
        print(''.join(map(str, result180[i])), end=' ')
        print(''.join(map(str, result270[i])), end='\n')