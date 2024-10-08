s = input()
tmp = ''
answer = ''
for i in s:
    tmp += i
    if i == ">":
        answer += tmp
        tmp = ''
    elif i == "<":
        answer += tmp[:-1][::-1]
        tmp = '<'
    elif i == " ":
        if tmp[0] == "<":
            pass
        else:
            answer += tmp[:-1][::-1] + ' '
            tmp = ''

print(answer+tmp[::-1])