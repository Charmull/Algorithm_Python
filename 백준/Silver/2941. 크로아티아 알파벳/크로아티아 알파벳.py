import sys

word = sys.stdin.readline().strip()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for el in cro:
    tmp = word.count(el)
    if tmp:
        count += tmp
        word = word.replace(el, ' ')
    
for el in word:
    if el != ' ':
        count += 1
print(count)