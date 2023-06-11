def solution(id_pw, db):
    for data in db:
        if id_pw[0] == data[0]:
            if id_pw[1] == data[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"