n = int(input())
w = int(input())

m = n*10
if n >= 5:
    m += 70
elif n >= 3:
    m += 20

if w > 1000:
    m -= 15

print(max(m, 0))