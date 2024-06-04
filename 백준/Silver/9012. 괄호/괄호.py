import sys

stack = []
for _ in range(int(sys.stdin.readline())):
    vps = sys.stdin.readline()
    for i in range(len(vps)):
        if vps[:i].count("(") < vps[:i].count(")"):
            print("NO")
            break
    else:
        if vps.count("(") != vps.count(")"):
            print("NO")
        else:
            print("YES")

