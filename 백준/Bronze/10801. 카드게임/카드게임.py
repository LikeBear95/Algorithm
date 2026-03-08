a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0

for i in range(10):
    if a[i] > b[i]:
        c += 1
    elif a[i] < b[i]:
        c -= 1

if c > 0:
    print("A")
elif c < 0:
    print("B")
else:
    print("D")