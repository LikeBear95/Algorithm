answer = 0
now = 0
for _ in range(4):
    a, b = map(int, input().split())
    now = now - a + b
    if answer < now:
        answer = now

print(answer)