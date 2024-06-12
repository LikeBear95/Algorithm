import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque(enumerate(map(int, sys.stdin.readline().split())))

for _ in range(n):
    idx, tmp = queue.popleft()
    print(idx + 1, end=" ")
    if tmp > 0:
        queue.rotate(1-tmp)
    else:
        queue.rotate(-tmp)
