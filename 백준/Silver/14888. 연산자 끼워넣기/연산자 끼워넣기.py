import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))  # +, -, *, //

max_num = [-1_000_000_000]
min_num = [1_000_000_000]
def dfs(idx, cur_op, total):
    if idx >= N:
        max_num[0] = max(max_num[0], total)
        min_num[0] = min(min_num[0], total)
        return

    for i in range(4):
        if oper[i] > cur_op[i]:
            cur_op[i] += 1
            tmp = total
            if i == 0:
                tmp += nums[idx]
            elif i == 1:
                tmp -= nums[idx]
            elif i == 2:
                tmp *= nums[idx]
            elif i == 3:
                if total < 0:
                    tmp = -(-tmp // nums[idx])
                else:
                    tmp //= nums[idx]
            dfs(idx + 1, cur_op, tmp)
            cur_op[i] -= 1


dfs(1, [0, 0, 0, 0], nums[0])
print(max_num[0])
print(min_num[0])