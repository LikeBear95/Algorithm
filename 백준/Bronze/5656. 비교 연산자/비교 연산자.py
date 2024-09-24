n = 1
while True:
    a, b, c = input().split()
    if b == "E":
        break
    if b == '>':
        answer = int(a) > int(c)
    elif b == '>=':
        answer = int(a) >= int(c)
    elif b == '<':
        answer = int(a) < int(c)
    elif b == '<=':
        answer = int(a) <= int(c)
    elif b == '==':
        answer = int(a) == int(c)
    elif b == '!=':
        answer = int(a) != int(c)

    print(f'Case {n}: {str(answer).lower()}')
    n += 1