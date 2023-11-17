T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort()
    is_poss = people[0] >= m
    
    cur_num = 0
    idx = 0
    for i in range(m, 11111):
        if not is_poss or idx >= n:
            break
        if not i % m:
            cur_num += k
        while idx < n and people[idx] <= i:
            if cur_num:
                cur_num -= 1
                idx += 1
                continue
            is_poss = False
            break
            
    print(f'#{test_case}', 'Possible' if is_poss else 'Impossible')