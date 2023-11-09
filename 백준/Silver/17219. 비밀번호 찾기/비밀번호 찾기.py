import sys

input = sys.stdin.readline
n, m = map(int, input().split())
site_pw = dict()

for _ in range(n):
    site, pw = input().split()
    site_pw[site] = pw
    
for _ in range(m):
    site = input().strip()
    print(site_pw[site])