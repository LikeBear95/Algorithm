while True:
    n = input()
    if n == '0':
        break
    while int(n) >= 10:
        n = str(sum([int(x) for x in n]))
    print(n)