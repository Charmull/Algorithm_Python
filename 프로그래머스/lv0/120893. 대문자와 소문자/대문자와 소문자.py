def solution(my_string):
    answer = ''
    for val in my_string:
        if val.islower():
            answer += val.upper()
        else:
            answer += val.lower()
    return answer