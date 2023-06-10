def solution(n):
    if n == 0: return 0
    answer = 0
    total = 1
    for i in range(1, 11):
        total *= i
        if total == n:
            answer = i
            break
        elif total > n:
            answer = i - 1
            break
    return answer