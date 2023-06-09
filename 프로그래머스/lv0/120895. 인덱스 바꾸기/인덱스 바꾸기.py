def solution(my_string, num1, num2):
    tmp = list(my_string)
    tmp[num1], tmp[num2] = tmp[num2], tmp[num1]
    return ''.join(tmp)