def solution(my_string):
    my_list = my_string.split()
    answer = int(my_list[0])
    for i in range(1, len(my_list), 2):
        if my_list[i] == '+':
            answer += int(my_list[i + 1])
        else:
            answer -= int(my_list[i + 1])
    return answer


"""
def solution(my_string):
    my_list = my_string.split()
    answer = int(my_list[0])
    for i in my_list[1:]:
        try:
            operand = int(i)
            if operator == '+':
                answer += operand
            else:
                answer -= operand
        except:
            operator = i
    return answer
"""

"""
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
"""

"""
def solution(my_string):
    return eval(my_string)
"""
