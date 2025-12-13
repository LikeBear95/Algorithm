n = 18446744073709551616 - int(input())
c = 0

while True:
    if n == 1:
        print(64-c)
        break
    else:
        n //= 2
        c += 1