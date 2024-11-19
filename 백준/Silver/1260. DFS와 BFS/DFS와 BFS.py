from collections import deque

def DFS(start):
    visited[start] = True
    print(start, end=" ")
    
    for i in sorted(l[start]):
        if not visited[i]:
            visited[i] = True
            DFS(i)

def BFS(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        tmp = queue.popleft()
        for i in sorted(l[tmp]):
            if not visited[i]:
                visited[i] = True
                queue.append(i)
        print(tmp, end=" ")
        
        
n,m,v = map(int, input().split())
l = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    l[s].append(e)
    l[e].append(s)

visited = [False] * (n+1)
DFS(v)
print()
visited = [False] * (n+1)
BFS(v)
