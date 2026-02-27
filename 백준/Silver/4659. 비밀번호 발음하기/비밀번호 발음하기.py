import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == "end":
        break
        
    a, b = "", ""
    c = 0
    
    for i in s:
        if i in ['a','e','i','o','u']:
            a += i
            b = ""
            c += 1
        else:
            a = ""
            b += i

        if len(a)+len(b) >= 3:
            print(f'<{s}> is not acceptable.')
            break

        if i not in ['e', 'o'] and a.count(i)+b.count(i) >= 2:
            print(f'<{s}> is not acceptable.')
            break

    else:
        print(f'<{s}> is {"" if c else "not "}acceptable.')

