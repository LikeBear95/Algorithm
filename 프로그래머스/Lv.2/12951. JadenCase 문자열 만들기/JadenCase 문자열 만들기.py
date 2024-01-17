def solution(s):
    lst = list(map(str, s.split(' ')))
    tmp = []
    for word in lst:
        if not word:
            tmp.append(word)
        elif word[0].isdigit():
            tmp.append(word.lower())
            print(word)
        else:
            tmp.append(word.title())
            print(word)
    return ' '.join(tmp)