import sys
input = sys.stdin.readline

i = 1
while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    print(f"Triangle #{i}");
    i += 1

    if c == -1:
        print(f"c = {(a*a + b*b)**0.5:.3f}")
    elif a == -1 and c > b:
        print(f"a = {(c*c - b*b)**0.5:.3f}")
    elif b == -1 and c > a:
        print(f"b = {(c*c - a*a)**0.5:.3f}")
    else:
        print("Impossible.")
    print()