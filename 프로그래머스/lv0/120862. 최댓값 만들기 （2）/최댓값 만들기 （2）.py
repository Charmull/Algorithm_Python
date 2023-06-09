def solution(numbers):
    numbers.sort()
    answer = numbers[-1] * numbers[-2] if numbers[-1] * numbers[-2] > numbers[0] * numbers[1] else numbers[0] * numbers[1]
    return answer