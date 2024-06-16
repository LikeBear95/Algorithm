import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())
worm = [0] * (n + 1)
link = [[] for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

def bfs(start):
    queue = deque([start])
    worm[start] = 1

    while queue:
        current = queue.popleft()

        for linked in link[current]:
            if not worm[linked]:
                worm[linked] = 1
                queue.append(linked)

bfs(1)
print(worm.count(1)-1)
