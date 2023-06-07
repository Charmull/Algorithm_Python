# 반복 최소화
def solution(n):
    answer = 0
    flag = False
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            answer += 1
        if i ** 2 == n:
            flag = True
    return answer * 2 - 1 if flag else answer * 2


"""
# 코드 단순화
def solution1(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0: answer += 1
    return answer
"""
