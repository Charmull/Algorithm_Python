# 위상정렬
import sys
from collections import defaultdict, deque

input = sys.stdin.readline
n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = defaultdict(list)

for _ in range(m):
    tmp = list(map(int, input().split()))
    # 담당한 가수 수가 0명 혹은 1명이면 continue
    if tmp[0] == 0 or tmp[0] == 1:
        continue
        
    for i in range(1, len(tmp) - 1):
        a = tmp[i]
        b = tmp[i + 1]
        indegree[b] += 1
        graph[a].append(b)
    
# 위상 정렬    
def get_result():
    result = []
    deq = deque()
    
    # indegree 0인 것(선수가 없는 것) deq에 추가
    for i in range(1, n + 1):
        if not indegree[i]:
            deq.append(i)
        
    while deq:
        cur = deq.popleft()
        result.append(cur)
        
        # cur 후수에 대해 indegree 업데이트
        for i in graph[cur]:
            indegree[i] -= 1
            # indegree 0이면 (선수가 없으면) deq에 추가
            if not indegree[i]:
                deq.append(i)
                
    # result 길이가 n개인지 확인 (n보다 작으면 순서 정하는 것이 불가능한 것)
    if len(result) < n:
        return [0]
    return result

result = get_result()
print('\n'.join(map(str, result)))