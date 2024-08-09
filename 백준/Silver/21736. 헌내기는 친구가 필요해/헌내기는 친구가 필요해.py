import sys
input = sys.stdin.readline

n, m = map(int, input().split())
campus = [input().rstrip() for _ in range(n)]
visited = [[0]*m for _ in range(n)]
lst = []
answer = 0

for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            lst.append((i, j))
            visited[i][j] = 1
            break

while lst:
    a, b = lst.pop(0)
    for i, j in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        if a+i >= 0 and b+j >= 0 and a+i < n and b+j < m and visited[a+i][b+j] == 0:
            visited[a+i][b+j] = 1
            if campus[a+i][b+j] != "X":
                lst.append((a+i, b+j))
            if campus[a+i][b+j] == "P":
                answer += 1

print(answer if answer else "TT")
