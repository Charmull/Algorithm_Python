import sys

input = sys.stdin.readline
input_str = input().strip()
result = 0
tmp = ''
isGetMinus = False
for el in input_str:
    if el.isdigit():
        tmp += el
        continue
    if isGetMinus:
        result -= int(tmp)
        tmp = ''
        continue
    if el == '-':
        isGetMinus = True
    result += int(tmp)
    tmp = ''

print(result - int(tmp) if isGetMinus else result + int(tmp))