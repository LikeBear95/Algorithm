from collections import deque

n, k = map(int, input().split())
queue = deque()
answer = []
count = 1

for i in range(n):
    queue.append(i+1)

while queue:
    tmp = queue.popleft()
    if count == k:
        count = 1
        answer.append(tmp)
    else:
        count += 1
        queue.append(tmp)

print(f"<{', '.join(map(str, answer))}>")
