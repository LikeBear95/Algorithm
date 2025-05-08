n = int(input())
lst = list(map(int, input().split()))

angry, now = 0, 0

for i in lst:
    if i:
        angry += 1
    else:
        angry -= 1
    now += angry

print(now)