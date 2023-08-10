import sys
from collections import deque

def make_team(want_list, visited, start):
    deq = deque([start])
    order = []
    log = set()

    while deq:
        student = deq.popleft()
        want = want_list[student]
        order.append(student) # while문 돌면서 방문한 요소들 담는 list
        log.add(student)

        if want in visited:
            visited.update(order)
            return 0
        # 고리 생김
        if want in log:
            visited.update(order)
            return len(order) - order.index(want)
        
        deq.append(want)
    
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    want_list = [-1] + list(map(int, input().split()))
    visited = set() # make_team 함수 실행 전에 방문한 요소들 담는 set
    count = n
    for i in range(1, n + 1):
        if i in visited:
            continue
        count -= make_team(want_list, visited, i)
    print(count)