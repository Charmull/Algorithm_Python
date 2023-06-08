def solution(array, height):
    array.sort(reverse=True)
    answer = 0
    for val in array:
        if val > height: answer += 1
    return answer