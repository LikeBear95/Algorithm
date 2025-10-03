n = int(input())
d = {-1:0, 0:0, 1:0}
for i in list(map(int, input().split())):
    d[i] += 1

if d[0] >= n/2:
    print("INVALID")
elif d[1] > d[-1]:
    print("APPROVED")
else:
    print("REJECTED")
