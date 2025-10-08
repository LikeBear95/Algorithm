import sys
input = sys.stdin.readline

n = 0
s = "+"

while True:
    t = input().rstrip()
    if t == "=":
        break
    elif t in "+-*/":
        s = t
    else:
        if s == "+":
            n += int(t)
        elif s == "-":
            n -= int(t)
        elif s == "*":
            n *= int(t)
        elif s == "/":
            n //= int(t)

print(n)