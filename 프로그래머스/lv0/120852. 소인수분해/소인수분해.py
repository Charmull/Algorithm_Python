def solution(n):
    answer = []
    for i in range(2, n + 1):
        if (n <= 1):
            break

        isprime = True
        for j in range(2, i):
            if i % j == 0:
                isprime = False
                break
        if isprime:
            if n % i == 0:
                answer.append(i)
            while (n % i == 0):
                n /= i
    return answer


"""
# for-else 활용
def solution(n):
    result = set()
    
    while True:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                n //= i
                result.add(i)
                break
        else:
            break
                
    result.add(n)
    
    return sorted(result)
"""
