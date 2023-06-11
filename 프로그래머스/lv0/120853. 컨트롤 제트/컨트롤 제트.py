def solution(s):
    answer = 0
    prev = 0
    for v in s.split():
        if v == 'Z':
            answer -= prev
        else:
            answer += int(v)
            prev = int(v)
    return answer