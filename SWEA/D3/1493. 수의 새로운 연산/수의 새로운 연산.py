T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    def get_point(x, y):
        mn = x + y - 1
        p = mn * (mn - 1) // 2 + x
        return p

    def get_xy(p):
        line = 1
        while p > line:
            p -= line
            line += 1
        return (p, line - p + 1)

    p, q = map(int, input().split())
    x1, y1 = get_xy(p)
    x2, y2 = get_xy(q)
    print(f'#{test_case}', get_point(x1 + x2, y1 + y2))