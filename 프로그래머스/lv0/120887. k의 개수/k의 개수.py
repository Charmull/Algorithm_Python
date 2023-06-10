def solution(i, j, k):
    answer = 0
    for v in range(i, j + 1):
        for v2 in list(str(v)):
            if v2 == str(k):
                answer += 1
    return answer