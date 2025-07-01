n = int(input())
l = list(map(int, input().split()))
s = int(input())
c = 0

for i in l:
    c += i//s
    c += 1 if i%s else 0

print(c*s)