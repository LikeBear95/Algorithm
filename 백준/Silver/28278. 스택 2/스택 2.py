import sys

stack = []
for _ in range(int(sys.stdin.readline())):
    i = sys.stdin.readline()
    try:
        n = int(i)
        if n == 2:
            if stack: print(stack.pop())
            else: print(-1)
        elif n == 3:
            print(len(stack))
        elif n == 4:
            if stack: print(0)
            else: print(1)
        elif n == 5:
            if stack: print(stack[-1])
            else: print(-1)
    except:
        n, m = map(int, i.split())
        stack.append(m)
