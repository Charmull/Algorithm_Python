n = int(input())

result = [0]
log = []

def is_valid(nx, ny):
    for x, y in log:
        if x == nx or y == ny:
            return False
        if x - y == nx - ny:
            return False
        if x + y == nx + ny:
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