c = 0

while True:
    c += 1
    d = 0
    o, w = map(int, input().split())
    if o == w == 0:
        break

    while True:
        s, n = map(str, input().split())
        if s == "#":
            if d == 1:
                print(f"{c} RIP")
            elif o*0.5 < w < o*2:
                print(f"{c} :-)")
            else:
                print(f"{c} :-(")
            break
        
        if s == "E":
            w -= int(n)
            if w <= 0 :
                d = 1
        elif s == "F":
            w += int(n)
        