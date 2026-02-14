n = int(input())

for i in range(1,n+1):
    print(f'Case #{i}: ', end='')
    t = int(input())
    if t <= 25:
        print("World Finals")
    elif t <= 1000:
        print("Round 3")
    elif t <= 4500:
        print("Round 2")
    else:
        print("Round 1")