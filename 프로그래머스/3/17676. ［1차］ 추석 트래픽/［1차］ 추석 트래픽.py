def solution(lines):
    answer = 0
    
    def make_timelog(lines):
        timelog = []
        points = []
        for el in lines:
            _, s, t = el.split()
            # s를 ms로 정리
            hh, mm, ss = s.split(':')
            ss, ms = ss.split('.')
            s = ((int(hh) * 60 + int(mm)) * 60 + int(ss)) * 1000 + int(ms)
            # t를 ms로 정리
            tmp = t[:-1].split('.')
            t = int(tmp[0]) * 1000
            if len(tmp) == 2:
                t += int(tmp[1])
                
            # 시작시간, 끝시간 추가
            timelog.append([s - t + 1, s])
            points.append(s - t + 1)
            points.append(s)
            
        timelog.sort()
        points.sort()
        return timelog, points
    
    timelog, points = make_timelog(lines)
    
    for point in points:
        st = point
        en = point + 999
        cnt = 0
        for log1, log2 in timelog:
            if st <= log1 <= en or st <= log2 <= en:
                cnt += 1
                continue
            if log1 <= st <= log2 or log1 <= en <= log2:
                cnt += 1
            #     continue
            # break
        answer = max(answer, cnt)
    
    return answer