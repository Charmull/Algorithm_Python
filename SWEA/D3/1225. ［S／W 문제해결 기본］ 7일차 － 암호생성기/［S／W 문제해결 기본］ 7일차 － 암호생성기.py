from collections import deque

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    t = int(input())
    nums = deque(map(int, input().split()))
    flag = True
    while flag:
        for i in range(1, 6):
            el = nums.popleft() - i
            if el <= 0:
                nums.append(0)
                flag = False
                break
            nums.append(el)
                
    print(f'#{test_case}', ' '.join(map(str, list(nums))))