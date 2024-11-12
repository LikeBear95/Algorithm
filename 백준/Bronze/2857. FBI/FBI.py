l = []
for i in range(5):
    s = input()
    if "FBI" in s:
        l.append(i+1)
        
if l:
    print(*l)
else:
    print("HE GOT AWAY!")
