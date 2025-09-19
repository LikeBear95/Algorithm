import sys
input = sys.stdin.readline

def F(n, m, t):
    if t == '+':
        return n+m
    elif t == '-':
        return n-m
    elif t == '*':
        return n*m
    elif t == '/':
        return n//m if n>0 and m>0 else -(abs(n)//abs(m))
        

a, x, b, y, c = map(str, input().rstrip().split())
a, b, c = map(int, [a,b,c])
d, e = F(F(a,b,x),c,y), F(a,F(b,c,y),x)
print(min(d,e))
print(max(d,e))