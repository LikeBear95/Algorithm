from collections import deque

n, m, k, x = map(int, input().split())
l = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for _ in range(m):
    s, e = map(int, input().split())
    l[s].append(e)

queue = deque([x])
visited[x] = 0

while queue:
    s = queue.popleft()
    for i in l[s]:
        if visited[i] == -1:
            visited[i] = visited[s] + 1
            queue.append(i)

result = [i for i in range(1, n + 1) if visited[i] == k]

if result:
    print(*result, sep='\n')
else:
    print(-1)
