from collections import defaultdict

T = int(input())
for test_case in range(1, T + 1):
    t = int(input())
    score = map(int, input().split())
    count = defaultdict(int)
    for el in score:
        count[el] += 1

    max_count = -1
    result = -1
    items = sorted(count.items(), key=lambda x: x[0])
    for k, v in items:
        if v >= max_count:
            max_count = v
            result = k

    print(f'#{test_case} {result}')