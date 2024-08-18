s = input()
if s[0] == "0":
    print(int(s[1:]))
elif len(s) == 4:
    print(20)
else:
    if s[1] == "0":
        print(10+int(s[2]))
    else:
        print(int(s[0])+int(s[1:]))