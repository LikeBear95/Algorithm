al = list(map(int, input().split()))
bl = list(map(int, input().split()))
l = []
for i in range(10):
    if al[i] > bl[i]:
        l.append("A")
    elif al[i] < bl[i]:
        l.append("B")
    else:
        l.append("D")

a = l.count("A")*3 + l.count("D")
b = l.count("B")*3 + l.count("D")

print(a, b)
if a>b: print("A")
elif a<b: print("B")
else: 
    for i in l[::-1]:
        if i == "A":
            print("A")
            break
        elif i == "B":
            print("B")
            break
    else:
        print("D")
