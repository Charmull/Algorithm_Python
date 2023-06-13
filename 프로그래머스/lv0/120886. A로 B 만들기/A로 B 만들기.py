# replace() 메소드 활용
def solution(before, after):
    for v in before:
        if v in after:
            after = after.replace(v, '', 1)
        else:
            return 0
    return 1


"""
# sorted() 함수 활용
def solution(before, after):
    return int(sorted(before) == sorted(after))
"""
