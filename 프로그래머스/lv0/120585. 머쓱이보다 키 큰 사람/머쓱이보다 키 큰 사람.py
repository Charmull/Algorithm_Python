def solution(array, height):
    array.sort(reverse=True)
    answer = 0
    for val in array:
        if val > height:
            answer += 1
    return answer


"""
# 배열의 메소드들 활용하기
def solution(array, height):
	array.append(height)
    array.sort(reverse=True)
    return array.index(height)
"""

"""
# 배열의 메소드들 활용하기
def solution(array, height):
	return sum(1 for a in array if a > height)
"""
