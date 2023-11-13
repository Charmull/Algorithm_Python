# 1. 현재 총 무게가 한칸씩 옮겨갔을때 새 트럭을 올릴 수 있는지 확인
#    올릴 수 있으면 올리고, 아니면 말기

import sys
from collections import deque

input = sys.stdin.readline
n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
current_we = 0
current_pos = [0] * n
current_is_bridge = deque([[0, trucks[0]]])

current_pos[0] = 1
current_we += trucks[0]
time = 1
i = 1

while current_is_bridge:
    for _ in range(len(current_is_bridge)):
        who = current_is_bridge.popleft()
        current_pos[who[0]] += 1
        if current_pos[who[0]] <= w:
            current_is_bridge.append(who)
        else:
            current_we -= who[1]

    if i < n and current_we + trucks[i] <= l:
        current_pos[i] += 1
        current_is_bridge.append([i, trucks[i]])
        current_we += trucks[i]
        i += 1
    time += 1

print(time)