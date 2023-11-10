# 1. 주사위를 해당 방향으로 굴린다.
#    - 현재 주사위 상태 업데이트, 현재 위치 업데이트
#    - 주사위 : 배열로 각 위치별 값을 저장
#           굴린 후 주사위의 새로운 위치값에 맞춰 배열을 업데이트
# 2. 해당 위치 지도 값이 0이면 주사위의 바닥면 값을 지도에 옮기고,
#    아니면 주사위의 바닥면에 값을 복사한 후 지도 값을 0으로 바꾼다.
#    - 현재 주사위 및 지도 업데이트
import sys

input = sys.stdin.readline
n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
pos = [x, y]
turn = list(map(int, input().split()))
dice = [0] * 7


def upd(dir):
    # 동
    if dir == 1:
        # 지도 바깥으로 이동 시
        if pos[1] + 1 < 0 or pos[1] + 1 >= m:
            return
        pos[1] += 1
        dice[3], dice[1], dice[4], dice[6] = dice[1], dice[4], dice[6], dice[3]
    # 서
    elif dir == 2:
        # 지도 바깥으로 이동 시
        if pos[1] - 1 < 0 or pos[1] - 1 >= m:
            return
        pos[1] -= 1
        dice[4], dice[1], dice[3], dice[6] = dice[1], dice[3], dice[6], dice[4]
    # 북
    elif dir == 3:
        # 지도 바깥으로 이동 시
        if pos[0] - 1 < 0 or pos[0] - 1 >= n:
            return
        pos[0] -= 1
        dice[2], dice[1], dice[5], dice[6] = dice[1], dice[5], dice[6], dice[2]
    # 남
    elif dir == 4:
        # 지도 바깥으로 이동 시
        if pos[0] + 1 < 0 or pos[0] + 1 >= n:
            return
        pos[0] += 1
        dice[6], dice[5], dice[1], dice[2] = dice[5], dice[1], dice[2], dice[6]

    if not board[pos[0]][pos[1]]:
        board[pos[0]][pos[1]] = dice[6]
    else:
        dice[6] = board[pos[0]][pos[1]]
        board[pos[0]][pos[1]] = 0
    print(dice[1])


for el in turn:
    upd(el)