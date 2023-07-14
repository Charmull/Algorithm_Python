n = int(input())
times = list(map(int, input().split()))
c1_list = [10 for _ in range(len(times))]
c2_list = [15 for _ in range(len(times))]
for i in range(len(times)):
    temp = times[i]
    while temp - 30 >= 0:
        c1_list[i] += 10
        temp -= 30
    temp = times[i]
    while temp - 60 >= 0:
        c2_list[i] += 15
        temp -= 60

if sum(c1_list) < sum(c2_list):
    print(f"Y {sum(c1_list)}")
elif sum(c1_list) > sum(c2_list):
    print(f"M {sum(c2_list)}")
else:
    print(f"Y M {sum(c1_list)}")