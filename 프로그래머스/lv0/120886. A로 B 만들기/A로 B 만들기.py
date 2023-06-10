def solution(before, after):
    for v in before:
        if v in after:
            after = after.replace(v, '', 1)
        else:
            return 0
    return 1