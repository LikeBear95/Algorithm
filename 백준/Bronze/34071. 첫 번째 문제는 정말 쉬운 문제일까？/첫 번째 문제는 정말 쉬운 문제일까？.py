n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))

if l[0] == min(l):
    print("ez")
elif l[0] == max(l):
    print("hard")
else:
    print("?")
