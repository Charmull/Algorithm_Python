import sys

n = int(sys.stdin.readline())
q_positions = []
result = [0]

def is_valid(r, c):
    for row, col in q_positions:
        if r == row or c == col:
            return False
        elif r - c == row - col:
            return False
        elif r + c == row + col:
            return False
    return True

def dfs(k):
    if len(q_positions) == n:
        result[0] += 1
        return
    
    for i in range(n):
        if not is_valid(k, i):
            continue
        q_positions.append((k, i))
        dfs(k + 1)
        q_positions.pop()
        
dfs(0)
print(result[0])