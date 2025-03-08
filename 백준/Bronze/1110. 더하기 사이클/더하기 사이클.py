n = int(input())
tmp = n
t = 0

while True:
    t += 1
    a = tmp//10
    b = tmp%10
    c = b*10 + (a+b)%10
    if c == n:
        break
    tmp = c

print(t)