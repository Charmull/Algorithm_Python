def solution(dots):
    x1 = dots[0][0]
    y1 = dots[0][1]
    x2, y2 = 0, 0
    for dot in dots[1:]:
        if dot[0] != x1:
            x2 = dot[0]
        elif dot[1] != y1:
            y2 = dot[1]
    return abs((x1 - x2) * (y1 - y2))