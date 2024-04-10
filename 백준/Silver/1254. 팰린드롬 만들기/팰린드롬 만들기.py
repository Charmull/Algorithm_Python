import sys

input = sys.stdin.readline
S = input().strip()

def is_palindrome(st):
    st = st
    en = len(S) - 1
    while st < en:
        if S[st] != S[en]:
            return False
        st += 1
        en -= 1
    return True

result = (len(S) - 1) * 2 + 1
for i in range(len(S)):
    if is_palindrome(i):
        result = len(S) - i + i * 2
        break

print(result)