n = 1000-int(input())
answer = 0
while True:
    if n >= 500:
        n -= 500
        answer += 1
    elif n >= 100:
        n -= 100
        answer += 1
    elif n >= 50:
        n -= 50
        answer += 1
    elif n >= 10:
        n -= 10
        answer += 1
    elif n >= 5:
        n -= 5
        answer += 1
    else:
        answer += n
        break

print(answer)