T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    result = 0
    building = list(map(int, input().split()))
    for i in range(2, n - 2):
        mn = max(building[i - 2], building[i -1], building[i + 1], building[i + 2])
        if mn >= building[i]:
            continue
        result += building[i] - mn
    print(f'#{test_case}', result)