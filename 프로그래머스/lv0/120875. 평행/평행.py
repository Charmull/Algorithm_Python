def solution(dots):
    answer = 0
    # for i in range(len(dots)):
    for j in range(1, len(dots)):
        rest = [0, 1, 2, 3]
        rest.remove(0)
        rest.remove(j)
        if abs((dots[0][0] - dots[j][0]) / (dots[0][1] - dots[j][1])) == abs((dots[rest[0]][0] - dots[rest[1]][0]) / (dots[rest[0]][1] - dots[rest[1]][1])):
            return 1
    return answer