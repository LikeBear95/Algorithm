import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(str, input().rstrip().split())
    sa, sb = {}, {}
    for i in a:
        if i in sa:
            sa[i] += 1
        else:
            sa[i] = 1
    for j in b:
        if j in sb:
            sb[j] += 1
        else:
            sb[j] = 1
    
    print(f'{a} & {b}', end=" ")
    print("are anagrams." if sa == sb else "are NOT anagrams.")