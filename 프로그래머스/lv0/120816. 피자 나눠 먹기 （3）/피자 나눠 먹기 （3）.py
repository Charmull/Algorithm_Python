def solution(slice, n):
    answer = 0
    if (n % slice) == 0:
        answer = n // slice
    else:
        answer = n // slice + 1
    return answer


"""
def solution(numbers):
    return ((n - 1) // slice) + 1
"""

"""
def solution(numbers):
	d, m = divmod(n, slice)
    return d + int(m != 0)
"""
