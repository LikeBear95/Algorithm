def solution(a, b):
    result1 = str(a) + str(b)
    result2 = str(b) + str(a)
    if int(result1) > int(result2):
        answer = int(result1)
    else:
        answer = int(result2)

    return answer