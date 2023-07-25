# 풀이 1
import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    deq = deque(sys.stdin.readline()[1:-2].split(','))
    error_flag = False
    reverse_count = 0

    if list(deq) == [''] and 'D' in p:
        print('error')
        continue
    
    for func in p:
        if func == 'R':
            reverse_count += 1
        else:
            if deq:
                if reverse_count % 2 == 0:
                    deq.popleft()
                else:
                    deq.pop()
            else:
                error_flag = True
                break

    if error_flag:
        print('error')
    else:
        if reverse_count % 2 == 0:
            print('[' + ','.join(deq) + ']')
        else:
            deq.reverse()
            print('[' + ','.join(deq) + ']')


# # 풀이 2
# import sys
# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#     p = list(map(len, input().rstrip().replace('RR', '').split('R')))
#     n = int(input())
#     if n == 0:
#         input()
#         arr = []
#     else:
#         arr = input().strip('[]\n').split(',')

#     # 앞에서부터 제거할 요소들의 개수를 담은 리스트(p[0::2])의 요소들을 합산
#     # 즉, front는 앞에서부터 제거할 요소의 개수
#     front = sum(p[0::2])
#     try:
#         # 뒤에서부터 제거할 요소들의 개수를 담은 리스트(p[1::2])의 요소들을 합산
#         # 즉, back은 뒤에서부터 제거할 요소의 개수
#         back = sum(p[1::2])
#     except:
#         back = 0

#     # 제거할 요소의 수가 n을 넘어서면
#     if front + back > n:
#         print('error')
#         continue
#     else:
#         # 요소를 제거
#         arr = arr[front:(n - back)]
    
#     if (len(p) + 1) % 2 == 1:
#         arr.reverse()
#     print('[' + ','.join(arr) + ']')