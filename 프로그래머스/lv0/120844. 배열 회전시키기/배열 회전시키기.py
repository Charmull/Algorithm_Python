def solution(numbers, direction):
    if direction == 'right':
        val = numbers.pop()
        numbers.insert(0, val)
    else:
        val = numbers.pop(0)
        numbers.append(val)
    return numbers