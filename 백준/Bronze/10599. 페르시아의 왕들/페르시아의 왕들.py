while True:
    a, b, c, d = map(int, input().rstrip().split())
    if a == b == c == d == 0:
        break
    print(abs(c-b), abs(d-a))