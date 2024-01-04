# 1. 이진 트리 기록하기 - 딕셔너리로 {부모:[자식들]}, 딕셔너리로 부모 정점 위치 담기
# 2. 두 정점의 공통부모 찾기 - 정점check set 두기
# 3. 공통부모의 서브 트리 개수 찾기 - dfs (재귀는 stack mem over될수도 있으니 스택으로)
# -> 정점이 v보다 클 수 있으니 딕셔너리로 두기

from collections import defaultdict

T = int(input())
for test_case in range(1, T + 1):
    v, e, target1, target2 = map(int, input().split())
    child = defaultdict(list)
    parent = defaultdict(int)
    rel = list(map(int, input().split()))
    for i in range(0, e * 2, 2):
        p = rel[i]
        c = rel[i + 1]
        child[p].append(c)
        parent[c] = p

    # 공통 부모 찾기
    visited_check = set()
    trg1_p = target1
    trg2_p = target2
    common_p = 0
    while True:
        if parent[trg1_p]:		# target1의 부모들을 찾고 set에 기록
            if parent[trg1_p] in visited_check:
                common_p = parent[trg1_p]
                break
            visited_check.add(parent[trg1_p])
            trg1_p = parent[trg1_p]
        if parent[trg2_p]:		# target2의 부모들을 찾고 set에 기록
            if parent[trg2_p] in visited_check:
                common_p = parent[trg2_p]
                break
            visited_check.add(parent[trg2_p])
            trg2_p = parent[trg2_p]

    # 공통부모의 서브트리 구하기
    child_num = len(child[common_p]) + 1
    deq = [child[common_p][0], child[common_p][1]]
    while deq:
        p = deq.pop()
        for i in child[p]:
            deq.append(i)
            child_num += 1

    print(f'#{test_case} {common_p} {child_num}')
