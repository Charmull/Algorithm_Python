# 1. 2*2 확인
# 2. 빈칸으로 변경
# 3. 내리기
def game(board, m, n):
    new_board = [[el for el in row] for row in board]
    is_bomb = False
    
    for i in range(m - 1):
        for j in range(n - 1):
            if not board[i][j]:
                continue
            tmp = board[i][j]
            if tmp == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                new_board[i][j] = ''
                new_board[i][j + 1] = ''
                new_board[i + 1][j] = ''
                new_board[i + 1][j + 1] = ''
                is_bomb = True
                
    return new_board, is_bomb

def upd_board(board, m, n):
    new_board = [[''] * n for _ in range(m)]
    
    for i in range(n):
        idx = m - 1
        for j in range(m - 1, -1, -1):
            if board[j][i]:
                new_board[idx][i] = board[j][i]
                idx -= 1
                continue
                
    return new_board
        
def cnt_bomb(board, m, n):
    cnt = 0
    for i in range(m):
        for j in range(n):
            if not board[i][j]:
                cnt += 1
                
    return cnt
    
def solution(m, n, board):
    answer = 0
    
    while True:
        turn = game(board, m, n)
        if not turn[1]:
            answer = cnt_bomb(board, m, n)
            break
        board = turn[0]
        board = upd_board(board, m, n)
    
    return answer