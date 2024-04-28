import sys

def sol(food, pigs):
    total = sum(pigs)
    days = 1
    while food >= total:
        total += total * 3
        days += 1
    return days

input = sys.stdin.readline
n = int(input())
for i in range(n):
    food = int(input())
    pigs = list(map(int, input().split()))
    print(sol(food, pigs))