n = int(input())
while True:
    t = int(input())
    if t == 0:
        break
    print(f'{t} is {"NOT " if t%n else ""}a multiple of {n}.')
