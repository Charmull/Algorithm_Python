def solution(A, B):
    for i in range(len(A)):
        if A != B:
            A = A[-1] + A[0:len(A) - 1]
        else:
            return i
    return -1