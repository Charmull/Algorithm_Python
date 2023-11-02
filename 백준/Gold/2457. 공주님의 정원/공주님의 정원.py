import sys

input = sys.stdin.readline
n = int(input())
flowers = []
for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    flowers.append([sm * 100 + sd, em * 100 + ed])
flowers.sort()

end_date = 301
count = 0

while flowers:
    if end_date >= 1201 or flowers[0][0] > end_date:
        break
        
    nxt_end_date = end_date
    for i in range(len(flowers)):
        if flowers[0][0] <= end_date:
            if nxt_end_date < flowers[0][1]:
                nxt_end_date = flowers[0][1]
            flowers.remove(flowers[0])
        else:
            break
            
    end_date = nxt_end_date
    count += 1
    
print(0 if end_date < 1201 else count)