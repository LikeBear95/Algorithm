import sys
input = sys.stdin.readline

for i in range(int(input())):
    lst = list(map(str, input().split()))
    n = float(lst[0])
    for i in lst[1:]:
        if i == "@":
            n *= 3
        elif i == "%":
            n += 5
        elif i == "#":
            n -= 7

    print(f'{n:.2f}')