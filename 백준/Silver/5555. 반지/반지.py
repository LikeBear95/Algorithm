import sys
input = sys.stdin.readline

s = input().rstrip()
answer = 0

for _ in range(int(input())):
    tmp = input().rstrip()
    if s in (tmp+tmp):
        answer += 1

print(answer)