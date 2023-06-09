def solution(rsp):
    answer = ''
    for i in rsp:
        answer += '0' if i == '2' else '5' if i == '0' else '2'
    return answer