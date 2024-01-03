def solution(spell, dic):
    answer = 2
    for string in dic:
        for alpha in spell:
            if not alpha in string:
                break
        else:
            return 1
    return answer