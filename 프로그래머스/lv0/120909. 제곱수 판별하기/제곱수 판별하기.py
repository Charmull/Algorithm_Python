def solution(n):
    answer = 1 if (n ** (1/2)) == int(n ** (1/2)) else 2
    return answer