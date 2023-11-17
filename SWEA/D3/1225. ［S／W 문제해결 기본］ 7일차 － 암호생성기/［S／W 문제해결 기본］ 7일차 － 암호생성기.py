from collections import deque

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    t = int(input())
    nums = deque(map(int, input().split()))
    div = min(nums) // 15
    for i in range(8):
        nums[i] -= 15 * (div - 1)
        
    find_result = False
    while not find_result:
        for i in range(1, 6):
            cur = nums.popleft() - i
            if cur <= 0:
                nums.append(0)
                find_result = True
                break
            nums.append(cur)
                
    print(f'#{test_case}', ' '.join(map(str, list(nums))))