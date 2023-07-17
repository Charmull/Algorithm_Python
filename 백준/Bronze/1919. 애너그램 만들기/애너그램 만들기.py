# 풀이 1
a, b = input(), input()
a = sorted(a)
b = sorted(b)
count = 0
while len(a) and len(b):
    if a[0] != b[0]:
        if a[0] in b:
            target_idx = b.index(a[0])
            b = b[target_idx:]
            count += target_idx
        elif b[0] in a:
            target_idx = a.index(b[0])
            a = a[target_idx:]
            count += target_idx
        else:
            a = a[1:]
            b = b[1:]
            count += 2
        continue
    a = a[1:]
    b = b[1:]

if a or b:
    count += len(a) + len(b)

print(count)


# # 풀이 2
# a = input()
# b = input()

# for i in a:
#   if i in b:
#     a = a.replace(i,'',1)
#     b = b.replace(i,'',1)

# print(len(a) + len(b))