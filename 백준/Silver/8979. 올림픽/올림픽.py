import sys

input = sys.stdin.readline
n, k = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]
country.sort(key=lambda x: (-x[1], -x[2], -x[3]))

result = 1
tmp = 0
if country[0][0] == k:
    print(result)
    sys.exit(0)

for i in range(1, n):
    if country[i - 1][1:] == country[i][1:]:
        tmp += 1
        if country[i][0] == k:
            print(result)
            break
        continue
    if tmp:
        result += tmp
        tmp = 0
    result += 1

    if country[i][0] == k:
        print(result + tmp)
        break