import sys
input = sys.stdin.readline

s = input().strip()
tmp = '0'
pm = True
answer = 0
for i in s:
    if i.isdecimal():
        tmp += i
    else:
        if pm:
            answer += int(tmp)
        else:
            answer -= int(tmp)
        tmp = ''
        if i == '-':
            pm = False

print(answer + int(tmp) if pm else answer - int(tmp))