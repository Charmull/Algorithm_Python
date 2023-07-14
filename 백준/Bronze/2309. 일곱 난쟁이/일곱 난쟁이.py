height_list = []
for i in range(9):
    height_list.append(int(input()))
    
over = sum(height_list) - 100
del_idx = []
for i in range(9):
    for j in range(i + 1, 9):
        if height_list[i] + height_list[j] == over:
            del_idx.append(i)
            del_idx.append(j)
            break
del height_list[del_idx[0]]
del height_list[del_idx[1] - 1]

print('\n'.join(map(str, sorted(height_list))))