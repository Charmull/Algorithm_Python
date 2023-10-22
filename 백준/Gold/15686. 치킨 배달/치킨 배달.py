import sys

input = sys.stdin.readline
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
homes = []
chickens = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            homes.append([i, j])
        elif city[i][j] == 2:
            chickens.append([i, j])

chicken_dis = []
for home in homes:
    tmp = []
    for chicken in chickens:
        tmp.append(abs(home[0] - chicken[0]) + abs(home[1] - chicken[1]))
    chicken_dis.append(tmp)
    
def get_total_dis(chicken_nums):
    total = 0
    for el in chicken_dis:
        tmp = 5000
        for i in chicken_nums:
            tmp = min(tmp, el[i])
        total += tmp
    return total
    
choices = []
result = [5000]
def choice_chicken(start, total_dis, count):
    if count == m:
        result[0] = min(result[0], get_total_dis(choices))
        return
    
    for i in range(start, len(chickens)):
        choices.append(i)
        count += 1
        choice_chicken(i + 1, total_dis, count)
        choices.remove(i)
        count -= 1
        
choice_chicken(0, 0, 0)
print(result[0])