from collections import deque

n, k = map(int, input().split())
queue = deque(range(1, n + 1))
answer = []
count = 1

while queue:
    tmp = queue.popleft()
    if count == k:
        count = 1
        answer.append(tmp)
    else:
        count += 1
        queue.append(tmp)

print(f"<{', '.join(map(str, answer))}>")
