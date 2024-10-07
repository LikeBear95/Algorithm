l = input()
for i in l:
    n = ord(i)
    if n >= 65 and n <= 90:
        n += 13
        if n > 90:
            n -= 26
    elif n >= 91 and n <= 122:
        n += 13
        if n > 122:
            n -= 26
    print(chr(n), end="")