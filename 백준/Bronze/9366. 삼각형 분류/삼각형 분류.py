n = int(input())

for i in range(n):
    print(f'Case #{i+1}: ', end='')
    a, b, c = map(int, input().split())
    if max(a,b,c)*2 >= sum([a,b,c]):
        print("invalid!")
    elif a == b == c:
        print("equilateral")
    elif a == b or b == c or c == a:
        print("isosceles")
    else:
        print("scalene")