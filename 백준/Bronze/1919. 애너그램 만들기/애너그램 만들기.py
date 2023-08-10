import sys

input = sys.stdin.readline
a = input().strip()
b = input().strip()
a_alph_nums = [0] * 26
b_alph_nums = [0] * 26
for v in a:
    a_alph_nums[ord(v) - ord('a')] += 1
for v in b:
    b_alph_nums[ord(v) - ord('a')] += 1

count = 0
for i in range(26):
    count += abs(a_alph_nums[i] - b_alph_nums[i])
print(count)