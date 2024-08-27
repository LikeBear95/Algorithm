a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
lst = A.difference(B)

print(len(lst))
if lst:
    print(*sorted(lst))