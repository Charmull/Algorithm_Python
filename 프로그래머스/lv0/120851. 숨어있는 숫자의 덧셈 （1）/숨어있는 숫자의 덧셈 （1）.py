def solution(my_string):
    answer = sum(int(val) for val in my_string if val in '0123456789')
    return answer