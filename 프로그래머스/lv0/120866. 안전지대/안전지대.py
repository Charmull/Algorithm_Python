def solution(board):
    n = len(board)
    safe_list = [[True] * n for _ in range(n)]

    around = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]

    def check(i, j):
        for x, y in around:
            if {i + x, j + y} & {-1, n}:
                continue
            safe_list[i+x][j+y] = False

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                check(i, j)

    return sum(sum(row) for row in safe_list)


"""
def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)
"""

"""
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
    check_board = [[0] * len(board) for i in range(len(board))]
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
"""
