for _ in range(int(input())):
    n = int(input())
    print("Bye" if (n+1)%int(str(n)[-2:]) else "Good")