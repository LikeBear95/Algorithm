answer = 0
for i in range(1, int(input())+1):
    if i % 125 == 0:
        answer += 3
    elif i % 25 == 0:
        answer += 2
    elif i % 5 == 0:
        answer += 1

print(answer)
