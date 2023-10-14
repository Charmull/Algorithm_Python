import sys

input = sys.stdin.readline
n, m = map(int, input().split())
log = []

def make_seq(log):
    if len(log) == m:
        print(' '.join(map(str, log)))
        return
    
    for i in range(1, n + 1):
        if i in log:
            continue
        log.append(i)
        make_seq(log)
        log.pop()
        
make_seq(log)