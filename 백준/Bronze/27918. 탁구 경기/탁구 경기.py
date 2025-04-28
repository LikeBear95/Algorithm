d, p = 0, 0

for _ in range(int(input())):
    s = input()
    if s == "D":
        d += 1
    elif s == "P":
        p += 1

    if abs(d-p) >= 2:
        break

print(f'{d}:{p}')