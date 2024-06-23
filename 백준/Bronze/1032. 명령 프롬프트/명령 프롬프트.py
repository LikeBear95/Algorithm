import sys
input = sys.stdin.readline

n = int(input())
answer = input()

for _ in range(n-1):
    tmp = input()
    for i in range(len(tmp)):
        if answer[i] != tmp[i]:
            answer = answer[:i] + "?" + answer[i+1:]

print(answer)
