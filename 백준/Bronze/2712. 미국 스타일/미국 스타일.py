import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, t = map(str, input().split())
    n = float(n)
    if t == "kg":
        print(f'{n*2.2046:.4f} lb')
    elif t == "lb":
        print(f'{n*0.4536:.4f} kg')
    elif t == "l":
        print(f'{n*0.2642:.4f} g')
    elif t == "g":
        print(f'{n*3.7854:.4f} l')