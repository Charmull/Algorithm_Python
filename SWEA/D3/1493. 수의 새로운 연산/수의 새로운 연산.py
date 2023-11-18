# 1,1 -> 1
# 1,2 -> 2 / 2,1 -> 3
# 1,3 -> 4 / 2,2 -> 5 / 3,1 -> 6
num = 1
arr1 = [[0] * 1000 for _ in range(1000)]
arr2 = [0]
for i in range(1, 1000):
    for j in range(i, 0, -1):
        arr1[i - j + 1][j] = num
        arr2.append((i - j + 1, j))
        num += 1
            
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    p, q = map(int, input().split())
    x1, y1 = arr2[p]
    x2, y2 = arr2[q]
    print(f'#{test_case}', arr1[x1 + x2][y1 + y2])
