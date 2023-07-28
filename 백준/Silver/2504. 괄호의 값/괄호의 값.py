# 풀이 2 / 재귀, 스택 사용
import sys

input_str = sys.stdin.readline().strip()

def go(string):
  if string == '':
    return []
  stack = []
  temp = []
  log = ''
  for v in string:
    if v == '(' or v == '[':
      stack.append(v)
    else:
      if v == ')':
        pair = '('
      else:
        pair = '['
      if not stack or stack.pop() != pair:
        print(0)
        sys.exit(0)

    log += v

    if stack == []:
      if log[0] == '(':
        num = 2
      else:
        num = 3

      if len(log) == 2:
        temp.append(num)
      else:
        temp.append([str(num) + '*', go(log[1:-1])])
      log = ''

  if stack:
    print(0)
    sys.exit(0)
  return temp


def cal(arr):
  if isinstance(arr, int):
    return arr

  if arr[0] == '2*':
    return 2 * cal(arr[1:])
  if arr[0] == '3*':
    return 3 * cal(arr[1:])

  return sum(map(lambda x: cal(x), arr))


arr = go(input_str)
print(cal(arr))


# # 풀이 3 / 스택만 사용
# import sys

# bracket = sys.stdin.readline().strip()
# length = len(bracket)
# stack = []
# num = 1
# total = 0

# for i in range(length):
#     b = bracket[i]
#     pair = '(' if b == ')' else '['
#     operand = 2 if b == ')' else 3

#     if b == '(':
#         num *= 2
#         stack.append(b)
#     elif b == '[':
#         num *= 3
#         stack.append(b)
#     else:
#         if not stack or stack[-1] != pair:
#             total = 0
#             break
#         if bracket[i-1] == pair:
#             total += num
#         num //= operand
#         stack.pop()

# if stack:
#     total = 0
# print(total)