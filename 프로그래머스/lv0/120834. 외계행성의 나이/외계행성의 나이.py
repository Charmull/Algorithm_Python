def solution(age):
    answer = ''
    age_str = str(age)
    while(age_str):
        val = age_str[0]
        answer += 'abcdefghij'[int(val)]
        age_str = age_str[1:]
    return answer