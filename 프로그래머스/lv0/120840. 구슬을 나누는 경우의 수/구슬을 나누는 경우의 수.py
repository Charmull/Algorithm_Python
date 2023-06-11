def solution(balls, share):
    answer = balls
    if balls == share: return 1
    for i in range(share - 1):
        balls -= 1
        answer *= balls
    for i in range(share):
        answer //= share
        share -= 1
    return answer