T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    t = int(input())
    matrix = [list(input().strip()) for _ in range(100)]
    result = [0]

    def find_long(arr):
        for i in range(100):
            for j in range(i + 1, 101):
                tmp1 = arr[i:j]
                tmp2 = tmp1[::-1]
                if tmp1 == tmp2:
                    result[0] = max(result[0], len(tmp1))
        for i in range(100, 0, -1):
            for j in range(1, i):
                tmp1 = arr[i-j:i]
                tmp2 = tmp1[::-1]
                if tmp1 == tmp2:
                    result[0] = max(result[0], len(tmp1))

    for i in range(100):
        tmp = matrix[i]
        find_long(tmp)

    for j in range(100):
        tmp = []
        for i in range(100):
            tmp.append(matrix[i][j])
        find_long(tmp)

    print(f'#{test_case}', result[0])