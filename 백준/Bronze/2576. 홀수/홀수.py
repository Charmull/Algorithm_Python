odd_list = []
for i in range(7):
    num = int(input())
    if num % 2 == 1: odd_list.append(num)

if odd_list:
    print(sum(odd_list))
    print(sorted(odd_list)[0])
else:
    print(-1)