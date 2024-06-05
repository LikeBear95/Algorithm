import sys

n = int(sys.stdin.readline())
stack1 = list(map(int, sys.stdin.readline().split()))
stack2 = []
cnt = 1

while stack1:
    if stack1[0] == cnt:
        stack1.pop(0)
        cnt += 1
    else:
        if stack2 and stack2[-1] == cnt:
            stack2.pop()
            cnt += 1
        else:
            stack2.append(stack1.pop(0))

if stack2 != sorted(stack2, reverse=True):
    print("Sad")
else:
    print("Nice")
