for _ in range(int(input())):
    n = int(input())
    print(0 if n%3 else 2**(n//3))