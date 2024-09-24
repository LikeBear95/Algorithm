answer = 10
s = input()
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        answer += 10
    else:
        answer +=5
print(answer)