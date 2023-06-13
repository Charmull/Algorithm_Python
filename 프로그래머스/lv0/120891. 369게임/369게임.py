def solution(order):
    answer = 0
    for val in str(order):
        if val in '369':
            answer += 1
    return answer


"""
# count() 메소드 활용
def solution(order):
    answer = 0
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')
"""

"""
# map() 메소드 활용
def solution(order):
	return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))
"""

"""
# sum() 함수 활용
def solution(order):
	return sum(n in '369' for n in str(order))
"""
