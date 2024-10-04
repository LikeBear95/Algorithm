lst = list(map(int, input().split()))
n = lst.index(20)
alice = (20 + lst[(n+1)%20] + lst[(n-1)%20]) / 3
bob = 10.5
if alice > bob:
    print("Alice")
elif alice < bob:
    print("Bob")
else:
    print("Tie")