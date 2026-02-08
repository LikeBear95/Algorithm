n = int(input())

if n >= 1000000:
    t = n//5
elif n >= 500000:
    t = n*3//20
elif n >= 100000:
    t = n//10
else:
    t = n//20

print(t, n-t)