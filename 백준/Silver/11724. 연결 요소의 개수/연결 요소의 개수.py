from collections import deque
import sys
input = sys.stdin.readline

def BFS(start):
    visited[start] = True
    queue = deque([start])

    while queue:
        tmp = queue.popleft()

        for i in l[tmp]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


n, m = map(int, input().split())
l = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    l[s].append(e)
    l[e].append(s)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        BFS(i)

print(count)