import sys
input = sys.stdin.readline

v = set('aeiou')

while True:
    s = input().rstrip()
    if s == "end":
        break
    
    p = ""
    a, b, c = 0, 0, 0
    
    for i in s:
        if i in v:
            a += 1
            b = 0
            c += 1
        else:
            a = 0
            b += 1

        if a >= 3 or b >= 3:
            print(f'<{s}> is not acceptable.')
            break

        if p == i and p not in ['e', 'o']:
            print(f'<{s}> is not acceptable.')
            break

        p = i

    else:
        print(f'<{s}> is {"" if c else "not "}acceptable.')
