def solution(quiz):
    answer = []
    for question in quiz:
        a, pm, b, eq, c = map(str, question.split())
        if pm == '+':
            if int(a) + int(b) == int(c):
                answer.append("O")
            else:
                answer.append("X")
        elif pm == '-':
            if int(a) - int(b) == int(c):
                answer.append("O")
            else:
                answer.append("X")
    return answer