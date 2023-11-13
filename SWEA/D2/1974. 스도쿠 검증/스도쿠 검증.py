T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    
    result = 1
    for i in range(9):
        count = [0] * 9
        if not result:
            break
        for j in range(9):
            count[matrix[i][j] - 1] += 1
            if count[matrix[i][j] - 1] > 1:
                result = 0
                break
        
    for j in range(9):
        count = [0] * 9
        if not result:
            break
        for i in range(9):
            count[matrix[i][j] - 1] += 1
            if count[matrix[i][j] - 1] > 1:
                result = 0
                break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            count = [0] * 9
            if not result:
                break
            for k in range(i, i + 3):
                for m in range(j, j + 3):
                    count[matrix[k][m] - 1] += 1
                    if count[matrix[k][m] - 1] > 1:
                        result = 0
                        break
                        
    print(f'#{test_case}', result)