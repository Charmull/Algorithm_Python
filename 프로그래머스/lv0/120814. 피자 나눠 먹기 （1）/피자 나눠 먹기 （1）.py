# 산술연산자와 삼항연산자 사용
def solution(n):
    answer = n / 7 if n % 7 == 0 else n // 7 + 1
    return answer


"""
# math의 ceil 함수 사용
from math import ceil

def solution(n):
    answer = ceil(n / 7)
    return answer
"""
