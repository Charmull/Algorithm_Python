# 풀이 2 / 37088KB, 3920ms
def solution():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    stack, answer = [], []
    now = 1
    for num in nums:
        while now <= num:
            stack.append(now)
            answer.append('+')
            now += 1
        if stack.pop() != num:
            return 'NO'
        answer.append('-')
    return '\n'.join(answer)

print(solution())


# # 풀이 1 / 36944KB, 5648ms
# n = int(input())
# lst = []
# stack = []
# for _ in range(n):
#     lst.append(int(input()))

# tmp = 1
# result = []
# while tmp <= n:
#     if len(stack) != 0 and stack[len(stack) - 1] == lst[0]:
#         stack.pop()
#         result.append('-')
#         del lst[0]
#     else:
#         stack.append(tmp)
#         result.append('+')
#         tmp += 1

# if tmp > n and stack == list(reversed(lst)):
#     result += ['-' for _ in stack]
#     print('\n'.join(result))
# else:
#     print("NO")