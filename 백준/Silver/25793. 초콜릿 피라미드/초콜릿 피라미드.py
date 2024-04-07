# 바닥층부터 층별로 계산
# 화이트는 2*r*c - r - c + 1
# 다크는 2*r*c - r - c
# r과 c의 차이로 식 간소화 후, 수식으로 한번에 계산
# - 예를 들어
#   r = c + 2
#   2*r*c = 2*(c^2 + 2c)
#   0부터 c까지 합산
# 시간복잡도: 100,000

import sys

input = sys.stdin.readline
t = int(input())


def make(r, c):
    diff = abs(r - c)
    if r < c:
        # 2 * (r ** 2 + r * diff) - 2 * r - diff
        #  = 2 * r**2 + 2*diff*r - 2*r - diff
        # r**2은 r * (r + 1) * (2*r + 1) // 6
        # r은 r * (r + 1) // 2
        # diff는 r * diff
        tmp = (r * (r + 1) * (2*r + 1) // 3) + \
            (r * (r + 1) * diff) - (r * (r + 1)) - r * diff
        white = tmp + r
        dark = tmp
    elif r > c:
        tmp = (c * (c + 1) * (2*c + 1) // 3) + \
            (c * (c + 1) * diff) - (c * (c + 1)) - c * diff
        white = tmp + c
        dark = tmp
    elif r == c:
        tmp = (c * (c + 1) * (2*c + 1) // 3) + \
            (r * (r + 1) * diff) - (r * (r + 1)) - r * diff
        white = tmp + r
        dark = tmp

    return white, dark


for _ in range(t):
    r, c = map(int, input().split())
    result = make(r, c)
    print(result[0], result[1])