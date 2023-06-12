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