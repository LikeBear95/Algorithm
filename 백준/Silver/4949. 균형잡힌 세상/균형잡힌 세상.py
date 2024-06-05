import sys

while True:
    vps = sys.stdin.readline().rstrip()
    if vps == ".":
        break
    lst = []
    for s in vps:
        if s == "(":
            lst.append("(")
        if s == "[":
            lst.append("[")
        if s == ")":
            try:
                tmp = lst.pop()
                if tmp != "(":
                    print("no")
                    break
            except:
                print("no")
                break
        if s == "]":
            try:
                tmp = lst.pop()
                if tmp != "[":
                    print("no")
                    break
            except:
                print("no")
                break
    else:
        if lst:
            print("no")
        else:
            print("yes")

