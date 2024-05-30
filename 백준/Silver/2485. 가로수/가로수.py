import math

n = int(input())
s = int(input())
lst = []

for _ in range(n - 1):
    tmp = int(input())
    lst.append(tmp - s)
    s = tmp

g = lst[0]
for i in range(1, len(lst)):
    g = math.gcd(g, lst[i])

answer = 0
for i in lst:
    answer += i // g - 1
print(answer)