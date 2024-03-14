answer = 0
for i in range(int(input())):
    word = input()
    tmp = []
    for i in range(len(word)):
        if word[i] not in tmp:
            tmp.append(word[i])
        elif word[i-1] != word[i]:
            break
    else:
        answer += 1

print(answer)