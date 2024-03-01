# dictionary 써서 A, B 문자열의 원소 개수들 기록
# 더 짧은 문자열의 dictionary 키를 돌면서 다른 문자열에 해당 키 개수 확인하고, 교집합 수 구하기
# 합집합 수 (A 개수 + B 개수 - 교집합 수) 구하기
# 자카드 유사도 계산
from collections import defaultdict
def solution(str1, str2):
    def make_dic(str, dict):
        cnt = 0
        for i in range(len(str) - 1):
            if 'A' <= str[i] <= 'Z' and 'A' <= str[i + 1] <= 'Z':
                dict[str[i:i + 2]] += 1
                cnt += 1
        return cnt
        
    str1 = str1.upper()
    str2 = str2.upper()
    str1_dic = defaultdict(int)
    str2_dic = defaultdict(int)
    str1_value_cnt = make_dic(str1, str1_dic)
    str2_value_cnt = make_dic(str2, str2_dic)
    
    a = 0
    for key, value in str1_dic.items():
        if str2_dic[key]:
            a += min(value, str2_dic[key])
            
    b = str1_value_cnt + str2_value_cnt - a
    
    if not a and not b:
        answer = 65536
    else:
        answer = int((a / b) * 65536)
    
    return answer