import sys
input = sys.stdin.readline

answer = 0
while True:
    try:
        answer += int(input())
    except:
        break

print(answer)