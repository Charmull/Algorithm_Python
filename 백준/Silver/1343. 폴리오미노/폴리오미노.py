import sys

input = sys.stdin.readline
board = input().strip().replace('XXXX', 'AAAA').replace('XX', 'BB')
print(-1 if 'X' in board else board)