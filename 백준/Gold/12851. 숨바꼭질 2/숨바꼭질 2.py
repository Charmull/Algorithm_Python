import sys
from collections import defaultdict

input = sys.stdin.readline
n, k = map(int, input().split())

def find_result():
    dic = defaultdict(int)  # 현재 시간에 도달할 수 있는 x 위치 : 현재 시간에 해당 위치에 도달한 개수
    dic[n] = 1
    visited = [0] * 100_001
    visited[n] = 1

    is_k = 0
    time = 0
    while not is_k:
        new_dic = defaultdict(int)
        for x, x_cnt in dic.items():
            for nx in (2 * x, x - 1, x + 1):
                if nx < 0 or nx > 100_000:
                    continue
                if visited[nx]:
                    continue
                new_dic[nx] += x_cnt
                if nx == k:
                    is_k += 1
        dic = new_dic
        for x in dic:
            visited[x] = 1
        time += 1

    return time, dic[k]

if n == k:
    print(0, 1, end='\n')
else:
    result = find_result()
    print(result[0], result[1], end='\n')