while(1):
    lst = list(map(int, input().split()))
    lst.sort()
    if lst == [0, 0, 0]:
        break

    if len(list(set(lst))) == 1:
        print("Equilateral")
    elif lst[2] >= lst[1] + lst[0]:
        print("Invalid")
    elif len(list(set(lst))) == 2:
        print("Isosceles")
    else:
        print("Scalene")