def solution(s):
    answer = [0, 0]
    while(s != "1"):
        answer[1] += s.count("0")
        tmp = s.count("1")
        num = ''
        while(tmp):
            num += str(tmp % 2)
            tmp //= 2
        s = num[::-1]
        answer[0] += 1
    return answer