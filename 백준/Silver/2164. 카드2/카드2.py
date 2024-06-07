import sys
from collections import deque

queue = deque()

for i in range(1, int(sys.stdin.readline())+1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(*queue)