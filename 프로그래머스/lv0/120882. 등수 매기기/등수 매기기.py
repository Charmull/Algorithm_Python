def solution(score):
    answer = [1 for i in range(len(score))]
    totalList = [v[0] + v[1] for v in score]
    for v1 in totalList:
        for i in range(len(totalList)):
            if v1 > totalList[i]: answer[i] += 1
    return answer