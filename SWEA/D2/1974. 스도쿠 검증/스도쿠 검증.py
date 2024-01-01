T = int(input())

# 가로, 세로 확인
def check1(board):
    for i in range(9):
        chk1 = [0] * 10
        chk2 = [0] * 10
        for j in range(9):
            # 가로 확인
            chk1[board[i][j]] += 1
            if chk1[board[i][j]] >= 2:
                return 0
            chk2[board[j][i]] += 1
            if chk2[board[j][i]] >= 2:
                return 0
    return 1

# 3*3 확인
def check2(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            chk = [0] * 10
            for ii in range(3):
                for jj in range(3):
                    chk[board[i + ii][j + jj]] += 1
                    if chk[board[i + ii][j + jj]] >= 2:
                        return 0
    return 1

for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    if check1(board) == 1 and check2(board) == 1:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')