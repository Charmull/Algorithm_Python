T = int(input())

# '.' 칸에 해당하는 숫자 찾아 적어놓기 + 0인 칸 기록


def make_result(board, n):
    result_board = [[el for el in row] for row in board]
    zero_idx = []
    for i1 in range(n):
        for j1 in range(n):
            if board[i1][j1] == '*':
                continue
            bomb_cnt = 0
            for i2 in (-1, 0, 1):
                for j2 in (-1, 0, 1):
                    if i1 + i2 < 0 or j1 + j2 < 0 or i1 + i2 >= n or j1 + j2 >= n:
                        continue
                    if board[i1 + i2][j1 + j2] == '*':
                        bomb_cnt += 1
            result_board[i1][j1] = bomb_cnt
            if not bomb_cnt:
                zero_idx.append([i1, j1])
    return result_board, zero_idx

# 클릭 업데이트


def click_upd(board, click_idx, result_board):
    if result_board[click_idx[0]][click_idx[1]] > 0:
        board[click_idx[0]][click_idx[1]
                            ] = result_board[click_idx[0]][click_idx[1]]
        return
    board[click_idx[0]][click_idx[1]] = 0
    for i in (-1 + click_idx[0],  click_idx[0], 1 + click_idx[0]):
        for j in (-1 + click_idx[1], click_idx[1], 1 + click_idx[1]):
            if i < 0 or j < 0 or i >= n or j >= n:
                continue
            if board[i][j] == '*':
                continue
            if board[i][j] == '.':
                if result_board[i][j] > 0:
                    board[i][j] = result_board[i][j]
                    continue
                click_upd(board, [i, j], result_board)


for test_case in range(1, T + 1):
    # 1. '.' 칸에 해당하는 숫자 찾아 적어놓기
    # 2. 0인 칸 먼저 클릭하도록 하기 (+연쇄 자동 클릭 함수 만들기)
    # 3. 0 외 숫자 칸 클릭하기
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    result_board, zero_idx = make_result(board, n)

    count = 0
    # 0인 칸 클릭
    for r, c in zero_idx:
        if board[r][c] != '.':
            continue
        click_upd(board, [r, c], result_board)
        count += 1
    # 0 외 숫자 칸 클릭
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                click_upd(board, [i, j], result_board)
                count += 1

    print(f'#{test_case} {count}')
