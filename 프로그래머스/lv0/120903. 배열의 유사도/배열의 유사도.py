def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
    return answer


"""
# 집합 자료형 set의 교집합 활용
def solution(numbers):
    return len(set(s1) & set(s2));
"""
