n = int(input())

for i in range(len(str(n))):
    d = 10**i
    n = (n+d//2)//d*d
    
print(n)
