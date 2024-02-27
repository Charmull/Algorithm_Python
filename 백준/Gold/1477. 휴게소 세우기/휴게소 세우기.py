# m개의 휴게소를 짓고 난 후에 휴게소가 없는 구간의 최댓값의 최솟값
# -> 휴게소가 없는 구간의 최댓값이 x면 휴게소 m개를 지을 수 있나?
# --> x에 대한 휴게소 개수 cnt 값이 단조감소 : 이분탐색
# --> x일 때 휴게소 개수 cnt가 m보다 크면 : cnt 줄이기, 즉 x 키우기
# --> x일 때 휴게소 개수 cnt가 m보다 작으면 : cnt 늘리기, 즉 x 줄이기
# --> x일 때 휴게소 개수 cnt가 m이면 : x가 더 작을때도 같은 cnt일 수도.
import sys

input = sys.stdin.readline
n, m, l = map(int, input().split())
store = [0] + list(map(int, input().split())) + [l]
store.sort()
diff = [store[i + 1] - store[i] for i in range(n + 1)]

def count_store(x):
    cnt = 0
    for i in range(n + 1):
        cnt += (diff[i] - 1) // x
    return cnt

st = 1
en = l - 1
while st < en:
    mid = (st + en) // 2
    cnt = count_store(mid)
    if cnt > m:
        st = mid + 1
    if cnt <= m:
        en = mid
        
print(st)