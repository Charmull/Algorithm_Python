# 스택에 한 문자씩 넣고, 현재 스택의 가장 뒤쪽에 위치한 문자열 일부가 폭발 문자열인지 확인 -> 맞으면 터뜨리기
import sys

input = sys.stdin.readline
st = list(input().strip())
st_len = len(st)
bumb = list(input().strip())
bumb_len = len(bumb)
stack = []
for i in range(st_len):
    stack.append(st[i])
    if len(stack) >= bumb_len and stack[-bumb_len:] == bumb:
        for _ in range(bumb_len):
            stack.pop()

print(''.join(stack) if stack else 'FRULA')