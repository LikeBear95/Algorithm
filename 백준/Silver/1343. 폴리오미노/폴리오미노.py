import sys
input = sys.stdin.readline

l = list(map(str, input().rstrip().split(".")))
x = ''

for i in l:
    if len(i)%2:
        print(-1)
        break
    else:
        x += 'AAAA'*(len(i)//4)+'B'*(len(i)%4)+'.'
else:
    print(x[:-1])