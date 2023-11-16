T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    board = [[0] * n for _ in range(n)]
    result = [0]
    
    def validation(r, c, n, board):
        for i in range(r):
            for j in range(n):
            	if board[i][j]:
                    if j == c:
                        return 0
                    if abs(i - r) == abs(j - c):
                        return 0
        return 1
                
    def count_nqueen(row, board):
        if row == n:
            result[0] += 1
            return
        for i in range(n):
            if validation(row, i, n, board):
                board[row][i] = 1
                count_nqueen(row + 1, board)
                board[row][i] = 0
                
    count_nqueen(0, board)
    print(f'#{test_case}', result[0])