l = [0] * 1001
for _ in range(int(input())):
    x, y = map(int, input().split())
    l[x] = y

left = [l[0]] + [0] * 1000
right = [0] * 1000 + [l[-1]]

for i in range(1, 1001):
    left[i] = max(left[i-1], l[i])
    right[1000-i] = max(right[1001-i], l[1000-i])

for i in range(1001):
    l[i] = min(left[i], right[i])

print(sum(l))
