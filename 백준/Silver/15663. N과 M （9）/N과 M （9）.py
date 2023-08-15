# 풀이 2
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
l = []
appended = [0] * n

def dfs():
    if len(l) == m:
        print(' '.join(map(str, l)))
        return
    
    prev = 0
    for i in range(n):
        if appended[i] or prev == nums[i]:
            continue
        l.append(nums[i])
        appended[i] = 1
        prev = nums[i]
        dfs()
        l.pop()
        appended[i] = 0
        
dfs()


# # 풀이 1
# import sys

# input = sys.stdin.readline
# n, m = map(int, input().split())
# nums = list(map(int, input().split()))
# nums.sort()
# l = []
# appended = [0] * n
# results = set()

# def dfs():
#     if len(l) == m:
#         if tuple(l) not in results:
#             print(' '.join(map(str, l)))
#             results.add(tuple(l))
#         return
    
#     for i in range(n):
#         if appended[i]:
#             continue
#         l.append(nums[i])
#         appended[i] = 1
#         dfs()
#         l.pop()
#         appended[i] = 0
        
# dfs()