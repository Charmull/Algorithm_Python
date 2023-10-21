import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
matrix = [[0] * m for _ in range(n)]

# 노트북의 x, y 위치에 스티커 붙일 수 있는지 확인
def pastable(x, y, r, c, paper):
	# 스티커 붙일 수 있는지 확인
	for i in range(r):
		for j in range(c):
			if matrix[x + i][y + j] == 1 and paper[i][j] == 1:
				return False

	# 스티커 붙이기
	for i in range(r):
		for j in range(c):
			if paper[i][j] == 1:
				matrix[x + i][y + j] = 1

	return True


def rotate(paper, r, c):
    tmp = []
    for i in range(r):
        tmp2 = []
        for j in range(c):
            tmp2.append(paper[i][j])
        tmp.append(tmp2)
	
    paper = [[0] * r for _ in range(c)]
    for i in range(c):
        for j in range(r):
            paper[i][j] = tmp[r - 1 - j][i]
    r, c = c, r
    return paper, r, c


for _ in range(k):
    r, c = map(int, input().split())
    sticker = []
    for i in range(r):
        sticker.append(list(map(int, input().split())))
        
    for rot in range(4):
        is_paste = False
        for x in range(n - r + 1):
            if is_paste:
                break
            for y in range(m - c + 1):
                if pastable(x, y, r, c, sticker):
                    is_paste = True
                    break
        if is_paste:
            break
        sticker, r, c = rotate(sticker, r, c)
        
count = 0
for i in range(n):
    for j in range(m):
        count += matrix[i][j]
print(count)