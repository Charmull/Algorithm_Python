# 크루스칼, 유니온 알고리즘
import sys

input = sys.stdin.readline
 
V, E = map(int, input().split())
Vroot = [i for i in range(V+1)]  # 해당 정점의 root (해당 정점과 연결된 정점 중 가장 작은값)
Elist = [list(map(int, input().split())) for _ in range(E)]
Elist.sort(key=lambda x: x[2])
 
# x 정점의 root(x 정점과 연결된 정점 중 가장 작은 값) 찾아주는 함수
def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]
 
answer = 0
for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        answer += w
        
print(answer)