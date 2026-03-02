a, b, c = map(int, input().split())
t = int(input())

if t <= 30:
    print(a)
else:
    print(a+(t+b-31)//b*c)