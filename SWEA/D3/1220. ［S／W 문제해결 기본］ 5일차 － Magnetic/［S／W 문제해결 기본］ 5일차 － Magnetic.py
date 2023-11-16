T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    result = 0
    
    for j in range(100):
        arr = []
        for i in range(100):
            if matrix[i][j]:
                arr.append(matrix[i][j])
        for i in range(len(arr) - 1):
            if arr[i] == 1 and arr[i + 1] == 2:
                result += 1
                
    print(f'#{test_case}', result)