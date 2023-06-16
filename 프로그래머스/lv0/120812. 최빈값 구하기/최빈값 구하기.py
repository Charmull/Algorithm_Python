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


"""
import collections

def solution(array):
    d = collections.Counter(array).most_common(2)
    print(d)
    if len(d) == 1 or d[0][1] != d[1][1]:
        return d[0][0]
    return -1
"""
