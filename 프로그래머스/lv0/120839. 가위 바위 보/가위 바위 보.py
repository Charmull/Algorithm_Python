def solution(rsp):
    answer = ''
    for i in rsp:
        answer += '0' if i == '2' else '5' if i == '0' else '2'
    return answer


"""
# 딕셔너리 이용
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)
"""

"""
# replace() 메소드 이용
def solution(rsp):
    rsp =rsp.replace('2','s')
    rsp =rsp.replace('5','p')
    rsp =rsp.replace('0','r')
    rsp =rsp.replace('r','5')
    rsp =rsp.replace('s','0')
    rsp =rsp.replace('p','2')
    return rsp
"""
