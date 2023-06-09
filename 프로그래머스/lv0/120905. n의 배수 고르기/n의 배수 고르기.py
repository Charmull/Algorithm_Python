def solution(n, numlist):
    answer = [val for val in numlist if val % n == 0]
    return answer