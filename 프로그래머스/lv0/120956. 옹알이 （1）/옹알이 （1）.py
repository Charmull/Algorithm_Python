def solution(babbling):
    answer = 0
    for v in babbling:
        for cond in ['aya', 'ye', 'woo', 'ma']:
            if v.count(cond) > 1:
                break
            elif v.count(cond) == 1:
                v = v.replace(cond, ' ')
        if v.replace(' ', '') == '':
            answer += 1
    return answer