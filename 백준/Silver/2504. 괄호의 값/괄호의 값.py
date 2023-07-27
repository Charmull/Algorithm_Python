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