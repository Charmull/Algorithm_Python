def solution(n):
    answer = 0
    flag = False
    for i in range(0, n):
        if n == 1:
            answer = 1
            flag = True
            break
        if n % (i + 1) == 0: answer += 1
        if (i + 1) * (i + 1) == n: flag = True
        if (i + 1) * (i + 1) <= n < (i + 2) * (i + 2): break
    return answer * 2 - 1 if flag else answer * 2