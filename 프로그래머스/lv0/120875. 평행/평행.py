def solution(dots):
    answer = 0
    for i in range(1, len(dots)):
        rest = [0, 1, 2, 3]
        rest.remove(0)
        rest.remove(i)
        if abs((dots[0][0] - dots[i][0]) / (dots[0][1] - dots[i][1])) == abs((dots[rest[0]][0] - dots[rest[1]][0]) / (dots[rest[0]][1] - dots[rest[1]][1])):
            return 1
    return answer


"""
def solution(dots):
    cases = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
    
    def get_slope(x, y):
        return (x[0] - y[0]) / (x[1] - y[1])

    for (a, b), (c, d) in cases:
        if get_slope(dots[a], dots[b]) == get_slope(dots[c], dots[d]):
            return 1

    return 0
"""

"""
def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]=dots
    answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
    answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
    answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))
    return 1 if answer1 or answer2 or answer3 else 0
"""
