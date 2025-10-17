import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    g = list(map(int, input().split()))
    s = list(map(int, input().split()))
    n = g[0]*1 + g[1]*2 + g[2]*3 + g[3]*3 + g[4]*4 + g[5]*10
    m = s[0]*1 + s[1]*2 + s[2]*2 + s[3]*2 + s[4]*3 + s[5]*5 + s[6]*10

    print(f"Battle {i+1}: ", end="")
    if n > m:
        print("Good triumphs over Evil")
    elif n < m:
        print("Evil eradicates all trace of Good")
    else:
        print("No victor on this battle field")