for _ in range(3):
    lst = list(map(int, input().split()))
    n = lst.count(0)
    if n == 0:
        print("E")
    elif n == 1:
        print("A")
    elif n == 2:
        print("B")
    elif n == 3:
        print("C")
    elif n == 4:
        print("D")