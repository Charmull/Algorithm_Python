def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            answer += i
    return answer


"""
# join() 활용
def solution(numbers):
    return "".join([i for i in my_string if not(i in "aeiou")])
"""
