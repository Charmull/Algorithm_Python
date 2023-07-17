def solution():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    stack, answer = [], []
    now = 1
    for num in nums:
        while now <= num:
            stack.append(now)
            answer.append('+')
            now += 1
        if stack.pop() != num:
            return 'NO'
        answer.append('-')
    return '\n'.join(answer)

print(solution())