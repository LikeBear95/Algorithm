import sys
input = sys.stdin.readline

answer = 0
for _ in range(int(input())):
    s = input().rstrip()
    if s == s[::-1]:
        answer += 1

print(answer*(answer-1))