a, b, c = map(int, input().split())
l = [0] * 101

for _ in range(3):
    s, e = map(int, input().split())
    for i in range(s, e):
        l[i] += 1
    
print(l.count(1)*a + l.count(2)*2*b + l.count(3)*3*c)