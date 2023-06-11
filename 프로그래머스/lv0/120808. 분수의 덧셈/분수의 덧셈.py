def solution(numer1, denom1, numer2, denom2):
    result_numer = (numer1 * denom2 + numer2 * denom1)
    result_denom = denom1 * denom2
    for i in range(2, min(result_numer, result_denom) + 1):
        while(result_numer % i == result_denom % i == 0):
            result_numer //= i
            result_denom //= i
        if result_numer == 1: break
    return [result_numer, result_denom]