a, b = map(int, input().split())
c = int(input())
s = a+b
print(s-2*c if s>=2*c else s)