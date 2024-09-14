n = int(input())
answer = 0
tmp = 1
while n > 0:
    if n >= tmp:
        n -= tmp
        tmp += 1
        answer += 1
    else:
        tmp = 1
print(answer)