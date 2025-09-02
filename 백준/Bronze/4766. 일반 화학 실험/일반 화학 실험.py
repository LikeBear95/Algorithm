t = float(input())

while True:
    x = float(input())
    if x == 999:
        break
    print(f'{x-t:.2f}')
    t = x