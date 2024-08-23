import sys
input = sys.stdin.readline

s = input().strip()
index = 0
length = len(s)

while index < length:
    if s[index:index+2] == "pi":
        index += 2
    elif s[index:index+2] == "ka":
        index += 2
    elif s[index:index+3] == "chu":
        index += 3
    else:
        print("NO")
        break
else:
    print("YES")
