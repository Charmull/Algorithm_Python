def solution(sides):
    answer = 0
    # 가장 긴 변이 sides 내에 있을 경우
    for i in range(1, max(sides)):
        if i + min(sides) > max(sides): answer += 1
    # 나머지 변이 가장 긴 변일 경우
    answer += sides[0] + sides[1] - max(sides)
    return answer