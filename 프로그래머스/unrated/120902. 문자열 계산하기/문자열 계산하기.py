def solution(my_string):
    answer = 0
    tmp = list(map(str, my_string.split()))
    for i, string in enumerate(tmp):
        if not i:
            answer += int(string)
        elif not i % 2:
            if tmp[i-1] == "+":
                answer += int(string)
            else:
                answer -= int(string)
            
    return answer