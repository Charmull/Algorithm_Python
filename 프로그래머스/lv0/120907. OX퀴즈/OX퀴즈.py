def solution(quiz):
    answer = []
    for q in quiz:
        list = q.split()
        if list[1] == '+':
            answer.append('O' if int(list[0]) + int(list[2]) == int(list[4]) else 'X')
        else:
            answer.append('O' if int(list[0]) - int(list[2]) == int(list[4]) else 'X')
    return answer