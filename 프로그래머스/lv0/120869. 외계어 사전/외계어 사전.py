def solution(spell, dic):
    answer = 2
    spellStr = sorted(''.join(spell))
    for v in dic:
        if sorted(v) == spellStr: return 1
    return answer