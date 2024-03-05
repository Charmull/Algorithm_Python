# 스택에 한 문자씩 넣고, 현재 스택의 가장 뒤쪽에 위치한 문자열 일부가 폭발 문자열인지 확인 -> 맞으면 터뜨리기
import sys

input = sys.stdin.readline
st = input().strip()
bomb = list(input().strip())
bomb_len = len(bomb)
stack = []
for s in st:
    stack.append(s)
    if stack[-bomb_len:] == bomb:
        for _ in range(bomb_len):
            stack.pop()

print(''.join(stack) if stack else 'FRULA')