import sys
input = sys.stdin.readline

s = input().rstrip()
answer = 0
for _ in range(int(input())):
    if s == input().rstrip():
        answer += 1
print(answer)