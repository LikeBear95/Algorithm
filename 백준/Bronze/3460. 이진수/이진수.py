for _ in range(int(input())):
    n = bin(int(input()))[2:]
    l = len(n)

    for i in range(l):
        if n[l-i-1] == "1":
            print(i, end=" ")
    print()
