def solution(my_string):
    my_list = my_string.split()
    operator = ''
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