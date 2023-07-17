k = int(input())
cal = []

for _ in range(k):
    num = int(input())
    if num == 0:
        if len(cal) != 0:
            cal.pop()
    else:
        cal.append(num)

print(sum(cal))