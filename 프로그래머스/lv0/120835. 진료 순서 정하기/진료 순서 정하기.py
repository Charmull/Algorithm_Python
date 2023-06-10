def solution(emergency):
    answer = []
    sorted_emg = sorted(emergency, reverse=True)
    for v in emergency:
        answer.append(sorted_emg.index(v) + 1)
    return answer