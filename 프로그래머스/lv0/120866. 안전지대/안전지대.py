def check_danger(board, i, j):
    if i - 1 < 0 and j - 1 < 0:
        board[i][j] = board[i][j + 1] = 2
        board[i + 1][j] = board[i + 1][j + 1] = 2
    elif i - 1 < 0 and j + 1 == len(board):
        board[i][j - 1] = board[i][j] = 2
        board[i + 1][j - 1] = board[i + 1][j] = 2
    elif i + 1 == len(board) and j - 1 < 0:
        board[i - 1][j] = board[i - 1][j + 1] = 2
        board[i][j] = board[i][j + 1] = 2
    elif i + 1 == len(board) and j + 1 == len(board):
        board[i - 1][j - 1] = board[i - 1][j] = 2
        board[i][j - 1] = board[i][j] = 2
    elif i - 1 < 0:
        board[i][j - 1] = board[i][j] = board[i][j + 1] = 2
        board[i + 1][j - 1] = board[i + 1][j] = board[i + 1][j + 1] = 2
    elif i + 1 == len(board):
        board[i - 1][j - 1] = board[i - 1][j] = board[i - 1][j + 1] = 2
        board[i][j - 1] = board[i][j] = board[i][j + 1] = 2
    elif j - 1 < 0:
        board[i - 1][j] = board[i - 1][j + 1] = 2
        board[i][j] = board[i][j + 1] = 2
        board[i + 1][j] = board[i + 1][j + 1] = 2
    elif j + 1 == len(board):
        board[i - 1][j - 1] = board[i - 1][j] = 2
        board[i][j - 1] = board[i][j] = 2
        board[i + 1][j - 1] = board[i + 1][j] = 2
    else:
        board[i - 1][j - 1] = board[i - 1][j] = board[i - 1][j + 1] = 2
        board[i][j - 1] = board[i][j] = board[i][j + 1] = 2
        board[i + 1][j - 1] = board[i + 1][j] = board[i + 1][j + 1] = 2


def solution(board):
    answer = 0
    check_board = [[0 for i in range(len(board))] for i in range(len(board))]
    if len(board) == 1:
        return 1 if board[0][0] == 0 else 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                # 위험지대 표시
                check_danger(check_board, i, j)
    for i in check_board:
        answer += i.count(0)
    return answer