s = [100, 100, 200, 200, 300, 300, 400, 400, 500]
l = list(map(int, input().split()))

for i in range(9):
    if s[i] < l[i]:
        print("hacker")
        break
else:
    if sum(l) >= 100:
        print("draw")
    else:
        print("none")