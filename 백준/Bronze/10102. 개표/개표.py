n = int(input())
s = input()
a = s.count("A")
b = s.count("B")
if a == b:
    print("Tie")
else:
    print("A" if a>b else "B")