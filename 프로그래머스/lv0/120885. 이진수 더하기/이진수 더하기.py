def solution(bin1, bin2):
    answer = ''
    if bin1 == bin2 == '0': return '0'
    over = 0
    bin1 = int(bin1)
    bin2 = int(bin2)
    while(bin1 or bin2 or over):
        result = bin1 % 10 + bin2 % 10 + over
        if result >= 2:
            over = 1
        else:
            over = 0
        answer = str(result % 2) + answer
        bin1 //= 10
        bin2 //= 10
    return answer