def solution(a, b):
    # 기약분수로 나타내기
    for i in range(2, min(a, b) + 1):
        if a % i == b % i == 0:
            a //= i
            b //= i
        if a == 1 or b == 1: break
    # 분모의 소인수가 2와 5만 있는지 확인
    while(True):
        if b % 2 == 0:
            b //= 2
        elif b % 5 == 0:
            b //= 5
        else:
            break
    return 1 if b == 1 else 2