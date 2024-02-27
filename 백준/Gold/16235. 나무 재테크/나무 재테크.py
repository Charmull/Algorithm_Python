from collections import deque
import sys
input = sys.stdin.readline

def main():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    land = [[5] * n for _ in range(n)]
    tree_matrix = [[deque() for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        x, y, z = map(int, input().split())
        tree_matrix[x - 1][y - 1].append(z)

    for _ in range(k):
        # 봄
        nutrient = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                alive = deque()
                tree_deq = tree_matrix[r][c]
                for tree in tree_deq:
                    if land[r][c] < tree:
                        break
                    land[r][c] -= tree
                    alive.append(tree + 1)
                for i in range(len(alive), len(tree_deq)):
                    dead_tree = tree_deq[i]
                    nutrient[r][c] += dead_tree // 2
                tree_matrix[r][c] = alive
        # 여름
        for r in range(n):
            for c in range(n):
                land[r][c] += nutrient[r][c]
        # 가을
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        new_tree = [[0] * (n + 2) for _ in range(n + 2)]
        for r in range(n):
            for c in range(n):
                for tree in tree_matrix[r][c]:
                    if tree % 5 != 0:
                        continue
                    for i, j in near:
                        nr, nc = r + i + 1, c + j + 1
                        new_tree[nr][nc] += 1
        for r in range(n):
            for c in range(n):
                num = new_tree[r + 1][c + 1]
                tree_matrix[r][c].extendleft([1] * num)
        # 겨울
        for r in range(n):
            for c in range(n):
                land[r][c] += a[r][c]
    # 출력
    count = 0
    for r in range(n):
        for c in range(n):
            count += len(tree_matrix[r][c])
    print(count)

if __name__ == '__main__':
    main()