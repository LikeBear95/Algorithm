s = input()
for i in s:
    n = ord(i)
    if n < 68:
        print(chr(n+23), end="")
    else:
        print(chr(n-3), end="")
