def solution(n):
    answer = 0
    for i in range(n):
        while(True):
            answer += 1
            if answer % 3 == 0 or '3' in str(answer):
                continue
            break
    return answer