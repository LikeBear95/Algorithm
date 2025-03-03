n = int(input())
x = 0
for i in range(0, n+1):
    for j in range(i, n+1):
        x += i+j

print(x)