# m명씩 n회 태울 수 있음. t분 간격으로 버스 옴
# 마지막 버스 오는 시간-> 09:00 + (n - 1) * t
# 마지막 버스 오는 시간에 타는 인원 수 확인
#  -> 2000명을 첫 버스부터 마지막 버스까지 태워보내보기
#  -> 마지막 버스가 가득 차면 -> 마지막 승객보다 1분 일찍 오기
#  -> 마지막 버스가 여유있으면 -> 마지막 버스 오는 시간 맞춰 오기
def solution(n, t, m, timetable):
    answer = ''
    changed_timetable = []
    for el in timetable:
        hour, min = list(map(int, el.split(':')))
        changed_timetable.append(hour * 60 + min)
    timetable = sorted(changed_timetable)
    
    bus_time = 9 * 60
    bus_cnt = 1
    person_idx = 0
    answer = 0
    while person_idx < len(timetable) and bus_cnt <= n:
        person_cnt = 0
        while person_cnt < m and person_idx < len(timetable) and timetable[person_idx] <= bus_time:
            person_cnt += 1
            person_idx += 1
            
        # 마지막 버스
        if bus_cnt == n:
            print(person_cnt, m, person_idx)
            if person_cnt < m:
                answer = bus_time
                break
            answer = timetable[person_idx - 1] - 1
            break
                
        bus_time += t
        bus_cnt += 1
        
    answer = str(answer // 60).zfill(2) + ':' + str(answer % 60).zfill(2)
    return answer