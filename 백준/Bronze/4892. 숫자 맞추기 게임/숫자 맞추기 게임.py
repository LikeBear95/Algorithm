tc = 0
while True:
    tc += 1
    n = int(input())
    if n == 0:
        break

    print(f"{tc}. {'odd' if n%2 else 'even'} {(n-1)//2 if n%2 else n//2}")