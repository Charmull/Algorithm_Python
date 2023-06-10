def solution(n):
    answer = 0
    if n < 4:
        return 0
    for i in range(4, n + 1):
        temp = 0
        for j in range(1, int(i ** (1/2)) + 1):
            if i % j == 0:
                temp += 1
                if temp >= 2: break
        if temp >= 2:
            answer += 1
            continue
    return answer