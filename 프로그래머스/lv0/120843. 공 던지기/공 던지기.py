def solution(numbers, k):
    answer = 0
    oddList = numbers[::2]
    evenList = numbers[1::2]
    if len(numbers) % 2 == 0:
        answer = oddList[(k - 1) % len(oddList)]
    else:
        if (k - 1) % len(numbers) <= len(oddList) - 1:
            answer = oddList[(k - 1) % len(numbers)]
        else:
            answer = evenList[(k - 1) % len(numbers) - len(oddList)]
    return answer