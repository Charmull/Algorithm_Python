def solution(common):
    answer = 0
    diff = 0
    ratio = 0
    if len(common) == 2:
        return common[1] + (common[1] - common[0])
    
    for i in range(1, len(common)):
        if diff != 0 and diff == common[i] - common[i - 1]:
            answer = common[-1] + diff
            break
        else:
            diff = common[i] - common[i - 1]
        if common[0] != 0:  
            if ratio != 0 and ratio == common[i] // common[i - 1]:
                answer = common[-1] * ratio
                break
            else:
                ratio = common[i] // common[i - 1]
    return answer