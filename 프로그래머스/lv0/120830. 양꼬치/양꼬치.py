def solution(n, k):
    main = n * 12000
    drink = (k - (n // 10)) * 2000
    answer = main + drink
    return answer