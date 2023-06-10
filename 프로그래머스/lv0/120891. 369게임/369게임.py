def solution(order):
    answer = 0
    for val in str(order):
        if val in '369':
            answer += 1
    return answer