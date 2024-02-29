from collections import deque

def solution(n, arr1, arr2):
    answer = []
    
    def change_num(num):
        deq = deque([])
        for _ in range(n):
            deq.appendleft(num % 2)
            num //= 2
        return list(deq)
    
    def make_map(map1, map2):
        result = []
        for i in range(n):
            if map1[i] == map2[i] == 0:
                result.append(' ')
                continue
            result.append('#')
        return ''.join(result)
    
    for i in range(n):
        answer.append(make_map(change_num(arr1[i]), change_num(arr2[i])))
    
    return answer