a, b = map(int, input().split())
if a % 2 and not b % 2:
    print((b-a+1)//2)
else:
    print((b-a+1)//2 + 1)