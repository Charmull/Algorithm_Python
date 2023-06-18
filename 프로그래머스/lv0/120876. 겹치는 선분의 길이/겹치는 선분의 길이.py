def solution(lines):
    sets = [set(range(l[0], l[1])) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])


"""
def solution(lines):
    answer = 0
    sorted_lines = sorted(lines, key=lambda x: (x[0], x[1]))
    # 겹치는 위치
    match_pos = []
    for i in range(3):
        for j in range(i + 1, 3):
            # 안 겹치는 경우
            if sorted_lines[i][1] <= sorted_lines[j][0]:
                pass
            elif sorted_lines[i][0] <= sorted_lines[j][0] and sorted_lines[i][1] >= sorted_lines[j][1]:
                match_pos.append(sorted_lines[j])
            elif sorted_lines[i][0] <= sorted_lines[j][0] and sorted_lines[j][0] <= sorted_lines[i][1]:
                match_pos.append([sorted_lines[j][0], sorted_lines[i][1]])
    if len(match_pos) == 1:
        return match_pos[0][1] - match_pos[0][0]
    else:
        match_pos.sort(key=lambda x: (x[0], x[1]))
        i = 0
        while (len(match_pos) - 1 >= i + 1):
            if match_pos[i][1] >= match_pos[i + 1][0]:
                match_pos.insert(i, [match_pos[i][0], max(
                    match_pos[i][1], match_pos[i + 1][1])])
                del match_pos[i + 1:i + 3]
            else:
                i += 1
        answer = sum(val[1] - val[0] for val in match_pos)
    return answer
"""

"""
def solution(lines):
    s1 = set(i for i in range(lines[0][0], lines[0][1]))
    s2 = set(i for i in range(lines[1][0], lines[1][1]))
    s3 = set(i for i in range(lines[2][0], lines[2][1]))
    return len((s1 & s2) | (s2 & s3) | (s1 & s3))
"""

"""
import collections

def solution(lines):
    counts = collections.defaultdict(int)
    
    for a, b in lines:
        for i in range(a, b):
            counts[i] += 1
    
    result = list(counts.values())
    
    return len(result) - result.count(1)
"""
