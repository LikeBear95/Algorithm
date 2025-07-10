n = int(input())
for i in range(n):
    l = sorted(list(map(int, input().split())))
    print(f"Scenario #{i+1}:")
    print("yes" if l[-1]**2 == l[0]**2 + l[1]**2 else "no")
    print()