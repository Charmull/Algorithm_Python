def solution(chicken):
    answer = chicken // 10
    restCoupon = chicken % 10 + answer
    while(chicken):
        chicken = restCoupon // 10
        answer += chicken
        restCoupon = restCoupon % 10 + chicken
    return answer

