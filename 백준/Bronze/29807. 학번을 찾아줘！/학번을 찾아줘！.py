n = int(input())
l = list(map(int, input().split())) + [0]*(5-n)
x = 0

if l[0] > l[2]:
    x += (l[0]-l[2])*508
else:
    x += (l[2]-l[0])*108

if l[1] > l[3]:
    x += (l[1]-l[3])*212
else:
    x += (l[3]-l[1])*305

x += l[4]*707

print(x*4763)