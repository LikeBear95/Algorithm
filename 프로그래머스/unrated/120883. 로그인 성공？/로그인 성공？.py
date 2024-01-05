def solution(id_pw, db):
    answer = 'fail'
    for idpw in db:
        if idpw == id_pw:
            answer = 'login'
            break
        elif idpw[0] == id_pw[0]:
            answer = 'wrong pw'
    return answer