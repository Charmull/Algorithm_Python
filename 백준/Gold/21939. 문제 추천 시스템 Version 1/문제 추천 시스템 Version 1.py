# 1. 난이도 높은순의 heapq, 낮은순의 heapq 두기
# 2. 현재 문제 리스트에 있으면 dict에 {문제번호: 난이도}로 넣고, 없으면 {문제번호: 0}
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
max_heap = []
min_heap = []
cur_p = defaultdict(int)    # 문제번호: 난이도 (제거되면 난이도는 0으로)
for _ in range(N):
    p, l = map(int, input().split())
    heapq.heappush(max_heap, (-l, -p))
    heapq.heappush(min_heap, (l, p))
    cur_p[p] = l

M = int(input())


def recommend(isMax):
    if isMax:
        h = max_heap
    else:
        h = min_heap
    tmp = -1 if isMax else 1
    while cur_p[h[0][1] * tmp] != h[0][0] * tmp:
        heapq.heappop(h)
    print(h[0][1] * tmp)


for _ in range(M):
    commend = input().split()
    if commend[0] == "add":
        p = int(commend[1])
        l = int(commend[2])
        cur_p[p] = l
        heapq.heappush(max_heap, (-l, -p))
        heapq.heappush(min_heap, (l, p))
    elif commend[0] == "recommend":
        if commend[1] == "1":
            # 어려운것
            recommend(True)
        elif commend[1] == "-1":
            # 쉬운 것
            recommend(False)
    elif commend[0] == "solved":
        cur_p[int(commend[1])] = 0