from collections import deque

def BFS():
    queue = deque([(0, 0, 1)])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        x, y, length = queue.popleft()

        if x == n - 1 and y == m - 1:
            return length

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '1' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, length + 1))

    return -1

n, m = map(int, input().split())
maze = [input().strip() for _ in range(n)]
visited = [[False] * m for _ in range(n)]
visited[0][0] = True

print(BFS())
