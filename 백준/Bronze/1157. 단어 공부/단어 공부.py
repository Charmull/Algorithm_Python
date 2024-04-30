text = input().upper()
element = set(text)
cnt = []
val = []

for i in element:
    val.append(i)
    cnt.append(text.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(val[cnt.index(max(cnt))])