n = int(input())
num = 1
for i in range(2, n + 1):
    num *= i
cnt = 0
while num:
    if num % 10:
        print(cnt)
        break
    cnt += 1
    num //= 10

if not num:
    print(0)