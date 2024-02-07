import sys

input = sys.stdin.readline
n, m = map(int, input().split())
pack = [list(map(int, input().split())) for _ in range(m)]
pack1 = sorted(pack, key=lambda x: x[0])
pack2 = sorted(pack, key=lambda x: x[1])
result = pack2[0][1] * n
result = min(result, pack1[0][0] * (n // 6) + pack2[0][1] * (n % 6))
if n % 6:
    result = min(result, pack1[0][0] * (n // 6 + 1))
print(result)