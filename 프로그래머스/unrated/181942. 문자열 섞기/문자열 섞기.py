def solution(str1, str2):
    answer = ''
    for i in range(len(str1) + len(str2)):
        if i % 2:
            answer += str2[i // 2]
        else:
            answer += str1[i // 2]
    return answer