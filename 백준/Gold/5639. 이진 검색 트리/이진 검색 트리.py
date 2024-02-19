# 1. 이진검색트리 구성하기 -> 딕셔너리
# 1.1. 전위순회로 들어옴
# 2. 후위순회 출력
# 2.1. DFS
import sys
from collections import defaultdict
sys.setrecursionlimit(int(1e5))

input = sys.stdin.readlines
tree = defaultdict(list)
nodes = input()
root = int(nodes[0])
tree[root] = [0, 0]
for i in range(1, len(nodes)):
    node = int(nodes[i])
    parent = root
    while True:
        if parent > node:
            if tree[parent]:
                if tree[parent][0]:
                    parent = tree[parent][0]
                    continue
                else:
                    tree[parent][0] = node
                    break
            else:
                tree[parent] = [node, 0]
                break
        elif parent < node:
            if tree[parent]:
                if tree[parent][1]:
                    parent = tree[parent][1]
                    continue
                else:
                    tree[parent][1] = node
                    break
            else:
                tree[parent] = [0, node]
                break

def dfs(cur):
    if tree[cur]:
        if tree[cur][0]:
            dfs(tree[cur][0])
        if tree[cur][1]:
            dfs(tree[cur][1])
    if cur:
        print(cur)

dfs(root)