def solution(array, n):
    answer = 100
    difference = 100
    for i in array:
        if abs(n - i) < difference:
            difference = abs(n - i)
            answer = i
        elif abs(n - i) == difference and i < answer:
            answer = i
        if difference == 0:
            break
    return answer


"""
# lambda, sorted() 활용
def solution(array, n):
    return sorted(array, key=lambda x: (abs(n - x), x))[0]
"""
