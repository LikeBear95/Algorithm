def solution(babbling):
    answer = 0
    for i in range(len(babbling)):
        for word in ['aya', 'ye', 'woo', 'ma']:
            if word in babbling[i]:
                babbling[i] = babbling[i].replace(word, '*')
                
        if all(string == '*' for string in babbling[i]):
            answer += 1
    return answer