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