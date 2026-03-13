import sys
input = sys.stdin.readline

l = list(map(str, input().rstrip().split()))


for s in l:
    if s in ["social", "history", "language", "literacy"]:
        print("digital humanities")
        break
    elif s in ["bigdata", "public", "society"]:
        print("public bigdata")
        break