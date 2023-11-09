import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dic_name = dict()
dic_num = dict()
for i in range(1, n + 1):
    name = input().strip()
    dic_name[name] = i
    dic_num[i] = name

for _ in range(m):
    question = input().strip()
    if question.isdecimal():
        print(dic_num[int(question)])
        continue
    print(dic_name[question])