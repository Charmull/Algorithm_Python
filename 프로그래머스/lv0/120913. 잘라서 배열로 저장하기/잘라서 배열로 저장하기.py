def solution(my_str, n):
    answer = []
    temp = ''
    for idx, v in enumerate(my_str):
        if idx != 0 and idx % n == 0:
            answer.append(temp)
            temp = ''
        temp += v
    answer.append(temp)
    return answer