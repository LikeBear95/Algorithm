s = input()

if len(s) % 2 == 0:  # 짝수 길이인 경우
    if s[:len(s)//2] == s[len(s)//2:][::-1]:
        print(1)
    else:
        print(0)
else:  # 홀수 길이인 경우
    if s[:len(s)//2] == s[len(s)//2+1:][::-1]:
        print(1)
    else:
        print(0)
