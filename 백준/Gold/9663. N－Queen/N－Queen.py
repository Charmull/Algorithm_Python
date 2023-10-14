n = int(input())
log = []
result = [0]

def is_valid(nx, ny):
    for x, y in log:
        if nx == x or ny == y:
            return False
        if nx - ny == x - y:
            return False
        if nx + ny == x + y:
            return False
    return True

def dfs(row):
    if len(log) == n:
        result[0] += 1
        return
    
    for col in range(n):
        if is_valid(row, col):
            log.append((row, col))
            dfs(row + 1)
            log.pop()
        
dfs(0)
print(result[0])