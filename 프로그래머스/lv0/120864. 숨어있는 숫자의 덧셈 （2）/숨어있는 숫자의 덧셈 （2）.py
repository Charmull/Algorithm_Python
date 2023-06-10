def solution(my_string):
    answer = 0
    temp = '0'
    for v in my_string:
        if v.isdigit():
            temp += str(v)
        else:
            answer += int(temp)
            temp = '0'
    
    if temp != '0':
        answer += int(temp)
    return answer