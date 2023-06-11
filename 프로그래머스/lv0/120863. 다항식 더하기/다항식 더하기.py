def solution(polynomial):
    inputList = polynomial.split()
    valX = 0
    valInt = 0
    for v in inputList:
        if v[-1] == 'x' and len(v) > 1:
            valX += int(v[:len(v) - 1])
        elif v[-1] == 'x':
            valX += 1
        elif v == '+':
            pass
        else:
            valInt += int(v)
    answer = ''
    if valX == 1:
        answer += 'x'
    elif valX != 0:
        answer += str(valX) + 'x'
    if valX != 0 and valInt != 0:
        answer += ' + ' + str(valInt)
    elif valX == 0 and valInt != 0:
        answer = str(valInt)
    return answer