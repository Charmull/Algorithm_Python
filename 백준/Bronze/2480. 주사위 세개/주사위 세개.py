l = list(map(int, input().split()))
if l[0] == l[1] == l[2]:
    print(10000 + l[0] * 1000)
elif l[0] == l[1] or l[0] == l[2] or l[1] == l[2]:
    l.sort()
    print(1000 + l[1] * 100)
else:
    l.sort()
    print(l[2] * 100)