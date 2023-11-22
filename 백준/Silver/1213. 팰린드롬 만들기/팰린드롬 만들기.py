from collections import defaultdict

string = input().strip()
dic = defaultdict(int)
for s in string:
    dic[s] += 1

keys = list(dic.keys())
keys.sort()
result = [''] * len(string)
for i in range(len(string) // 2):
    for key in keys:
        if dic[key] >= 2:
            result[i] = key
            result[len(string) - 1 - i] = key
            dic[key] -= 2
            break

if len(string) % 2:
    for key in keys:
        if dic[key]:
            result[len(string) // 2] = key

if '' in result:
    print('I\'m Sorry Hansoo')
else:
    print(''.join(map(str, result)))