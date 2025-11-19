n, r, c = map(int, input().split())
t = (r+c-2)%2
for i in range(n):
    for j in range(n):
        if (i+j)%2 == t:
            print("v", end="")
        else:
            print(".", end="")
    print()