k = int(input())
t, b = map(int, input().split())

if t == b:
    print(k**2)
else:
    print(k**2-(abs(t-b)/2)**2)