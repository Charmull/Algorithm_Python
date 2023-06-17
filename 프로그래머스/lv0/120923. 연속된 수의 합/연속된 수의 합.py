def solution(num, total):
    answer = []
    if num % 2 != 0:
        for i in range((total // num) - (num // 2), (total // num) + (num // 2) + 1):
            answer.append(i)
    else:
        for i in range((total // num) - (num // 2 - 1), (total // num) + (num // 2) + 1):
            answer.append(i)
    return answer


"""
def solution(num, total):
    q, r = divmod(num, 2)
    m = total // num + int(r == 0)
    return list(range(m - q, m + q + int(r != 0)))
"""
