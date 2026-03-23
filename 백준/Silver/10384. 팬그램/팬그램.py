import sys
input = sys.stdin.readline

for i in range(int(input())):
    l = [0] * 26
    for t in input().rstrip().lower():
        if 'a' <= t <= 'z':
            l[ord(t) - 97] += 1

    m = min(l)

    print(f'Case {i+1}: ', end="")
    if m == 0:
        print("Not a pangram")
    elif m == 1:
        print("Pangram!")
    elif m == 2:
        print("Double pangram!!")
    else:
        print("Triple pangram!!!")