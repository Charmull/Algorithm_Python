def solution(my_string):
    answer = sorted([int(v) for v in my_string if v in '0123456789'])
    return answer