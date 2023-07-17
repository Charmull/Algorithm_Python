n = int(input())
for _ in range(n):
    origin, strfry = input().split()
    print("Possible" if sorted(origin) == sorted(strfry) else "Impossible")