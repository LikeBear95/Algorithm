import sys
input = sys.stdin.readline

n = 0

while True:
    n += 1
    t = input().rstrip()
    if t == "0":
        break
    r, w, l = map(int, t.split())
    if (2*r)**2 >= w**2 + l**2:
        print(f"Pizza {n} fits on the table.")
    else:
        print(f"Pizza {n} does not fit on the table.")