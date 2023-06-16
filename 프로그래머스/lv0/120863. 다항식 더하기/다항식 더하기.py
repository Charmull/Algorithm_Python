def solution(polynomial):
    inputList = polynomial.split(' + ')
    valX = 0
    valInt = 0
    for v in inputList:
        if v[-1] == 'x':
            valX += 1 if v == 'x' else int(v[:-1])
        else:
            valInt += int(v)
            
    if valX == 0:
        return str(valInt)
    elif valX == 1:
        return 'x' if valInt == 0 else f'x + {valInt}'
    return f'{valX}x' if valInt == 0 else f'{valX}x + {valInt}'