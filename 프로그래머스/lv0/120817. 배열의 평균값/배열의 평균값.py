# list 요소의 합을 구하는 함수 sum 사용
def solution(numbers):
    answer = sum(numbers) / len(numbers)
    return answer


"""
# for문 사용
def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i
    answer /= len(numbers)
    return answer
"""
