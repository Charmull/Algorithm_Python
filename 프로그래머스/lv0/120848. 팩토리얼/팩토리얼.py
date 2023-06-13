def solution(n):
    answer = factorial = 1
    while n >= factorial:
        answer += 1
        factorial *= answer
    return answer - 1
