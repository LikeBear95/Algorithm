a, b = map(int, input().split())
print(2*b+1 if a>b else 2*min(a,b)-1)