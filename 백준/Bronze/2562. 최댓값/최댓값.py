max = 0
idx = -1
for i in range(9):
    temp = int(input())
    if max < temp:
        max = temp
        idx = i
print(max, idx + 1, sep='\n')