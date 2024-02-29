def solution(dartResult):
    dart_list = [int(dartResult[0])]
    for i in range(1, len(dartResult)):
        if '0' <= dartResult[i - 1] <= '9' and '0' <= dartResult[i] <= '9':
            dart_list.pop()
            dart_list.append(int(dartResult[i - 1]) * 10 + int(dartResult[i]))
            continue
        if '0' <= dartResult[i] <= '9':
            dart_list.append(int(dartResult[i]))
            continue
        dart_list.append(dartResult[i])
        
    
    score = [0, 0, 0]
    int_cnt = -1
    for i in range(len(dart_list)):
        cur = dart_list[i]
        try:
            cur = int(cur)
            int_cnt += 1
            score[int_cnt] = int(cur)
        except:
            if cur == 'S':
                score[int_cnt] **= 1
            elif cur == 'D':
                score[int_cnt] **= 2
            elif cur == 'T':
                score[int_cnt] **= 3
            elif cur == '*':
                score[int_cnt] *= 2
                if int_cnt:
                    score[int_cnt - 1] *= 2
            elif cur == '#':
                score[int_cnt] *= -1
                
    return sum(score)