def solution(array):
    answer = 0
    dedup = list(set(array))
    count = 0
    for i in dedup:
        if array.count(i) > count:
            answer = i
            count = array.count(i)
        elif count != 0 and array.count(i) == count:
            answer = -1
    return answer