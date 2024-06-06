import sys
from collections import deque

queue = deque()
for _ in range(int(sys.stdin.readline())):
    tmp = sys.stdin.readline().rstrip()
    if tmp == 'pop':
        if queue: print(queue.popleft())
        else: print(-1)
    elif tmp == 'size':
        print(len(queue))
    elif tmp == 'empty':
        print(0 if queue else 1)
    elif tmp == 'front':
        print(queue[0] if queue else -1)
    elif tmp == 'back':
        print(queue[-1] if queue else -1)
    else:
        queue.append(tmp[5:])
