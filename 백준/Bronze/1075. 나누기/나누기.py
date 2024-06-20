import sys
input = sys.stdin.readline

n = int(input())
f = int(input())

n = n // 100 * 100

if n % f == 0:
    print("00")
elif f - n % f < 10:
    print(f"0{f - n % f}")
else:
    print(f - n % f)
