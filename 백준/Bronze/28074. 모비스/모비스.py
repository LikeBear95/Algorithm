s = input()
for i in ["M", "O", "B", "I", "S"]:
    if i not in s:
        print("NO")
        break
        
else:
    print("YES")