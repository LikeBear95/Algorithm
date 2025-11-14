import sys
input = sys.stdin.readline

n = int(input())
total = 0

for _ in range(n):
    t = input().rstrip()
    if int(t) == 100:
        score = 100
    else:
        t = t.replace('0', '9').replace('6', '9')
        score = int(t)
        if score > 100:
            score = 100
    total += score

avg = total / n
result = int(avg + 0.5)

print(result)
