def solution(num_list, n):
    answer = []
    count = 0
    temp = []
    for i in num_list:
        temp.append(i)
        count += 1
        if count == n:
            answer.append(temp)
            temp = []
            count = 0
    return answer