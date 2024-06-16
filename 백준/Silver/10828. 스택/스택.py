import sys
from collections import deque
input = sys.stdin.readline

stack = deque()
for _ in range(int(input())):
    tmp = input().rstrip()
    if tmp == "pop":
        if stack: print(stack.pop())
        else: print(-1)
    elif tmp == "size":
        print(len(stack))
    elif tmp == "empty":
        if stack: print(0)
        else: print(1)
    elif tmp == "top":
        if stack: print(stack[-1])
        else: print(-1)
    else:
        stack.append(tmp[5:])
